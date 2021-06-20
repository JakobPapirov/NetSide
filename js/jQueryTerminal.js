$(document).ready(function() {
	/* 0.	This JS file will host anything related to the jQuery terminal
		Status: Prototype - 
		Docs: https://github.com/jcubic/jquery.terminal/wiki/Getting-Started
			Check out: 	Progress bar animation (Should be really cool with waiting for task to finish)
						Animation that emulate user typing
						Smooth CSS3 cursor animation (perhaps allow user customisation (paid?) )
						Emoji - perhaps userful
						Create Settings object from questions
						colors..something
						https://github.com/jcubic/jquery.micro (for allowing users to code!)
						https://github.com/jcubic/jquery.terminal/wiki/Saving-State
						https://github.com/jcubic/jquery.terminal/wiki/Formatting-and-Syntax-Highlighting
						https://github.com/jcubic/jquery.terminal/wiki/Parsing-commands
						https://github.com/jcubic/jquery.terminal/wiki/Tab-completion
			Q:	How to let users log in via the terminal?
					https://github.com/jcubic/jquery.terminal/wiki/Authentication
				Should other areas be rendered in the terminal as well?
				How to make sure the terminal keeps its size?
		Updated:
			2020-06-07
			2021-05-28 - 30
	*/

	// 1. Working code and semi-working code
		/*	https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#greetings
			greetings	works, however I'm getting error due not actually having the 'service.py' file
			prompt		works, but not together with greetings, probably because I need to pass multiple options inside an object
		*/	

		// 1.1 : Creates the terminal window
			$("#terminal-main").terminal(function(command){

				if (command !== '') {

					if (command == 'login') {

						this.echo('Type [[b;green;black]login help] for help.');
					} else if (command == 'login help') {

						this.echo('Type [[b;green;black]login user] to initiate login to server.');
					} else if (command == 'login user') {

						this.echo('Feature not yet implemented.');
					} else if (command == 'credits') {

						this.echo('[[!;i;black]https://terminal.jcubic.pl/]');
					} else {

						this.echo('Unrecognised command.');
					}
				}
			}, {
		        greetings: `Welcome to NetSide! You'll find the repo @ [[!;i;black]https://github.com/JakobPapirov/NetSide]\n
Available commands are:
[[b;green;black]login]
[[b;green;black]login help]
[[b;green;black]login user]
[[b;green;black]credits]\n`,
		        name: 'playArea',
		        height: 600,
		        width: '100%',
		        prompt: '>>> '
		    }, {
		    	// Has to be last, for everything to be read
		    	checkArity: false
			});
		// 1.2
			/*$("#terminal").terminal("../service.py", {

				greetings: "Welcome to Netside!"

				//prompt: "[[;red;]>>> ]"
			});*/
		// 1.3
			/*$('#terminal').terminal(function(command) {
		        if (command !== '') {
		            var result = window.eval(command);
		            if (result != undefined) {
		                this.echo(String(result));
		            }
		        }
		    }, {
		        greetings: 'Development in progress (last update on 2021-05-28)',
		        name: 'NetSide',
		        height: 298,
		        width: 930,
		        prompt: '>>> '
		    });*/
		// 1.4
			$('#terminal-commands').terminal({
		        add: function(a, b) {
		            this.echo(a + b);
		        },
		        // Hack; Want to nest inside 'add' really.
		        addHelp: function(...args) {
		        	this.echo("Command 'add' accepts two inputs: \n Type 'add input1 input2'.");
		        },
		        login: function() {

		        	this.echo("Login feature not yet complete.");
		        	// Works, but need to enter exact # of inputs
		        	/*if (help == 'help') {
		        		this.echo("Works!");
		        	} else {

		        	this.echo("Login feature not yet complete.");
		        	}*/
		        },
		        logout: function() {
		        	this.echo("Logout feature not yet complete.");
		        },
		        // Does nothing?
		        re: function(re, str) {
		           if (re instanceof RegExp && re.test(str)) {
		              this.echo(str + ' [[;green;]match]');
		           }
		        },
		        options: function(...args) {

		        	arrayCmds =	['add',
		        				 'addHelp',
		        				 'options',
		        				 'login',
		        				 'logout'];
		        	const output = displayCommands( arrayCmds );
		        	displayCommands( arrayCmds );

		        	// Splitting line doesn't work.
		        	this.echo(`${output}`);
		        }
		    }, {
		        greetings: "[[;blue;black]Game options terminal] \nDevelopment in progress (last update on 2021-05-28) \nDeveloped by: \nJakob Papirov\nType 'options' to see available commands.",
		        name: 'gameCommands',
		        height: '25vh',
		        width: '100%',
		        prompt: '>>> '
		    }, {
		    	// Has to be last, for everything to be read; allows for variable nr of inputs?
		    	checkArity: false
		    });

			// Terminal - notepad
				// Unused ->> VueJS attempt
				/*
		    $('#terminal-notepad').terminal(
		    {
		    	greetings: 'Notepad',
		        name: 'notepad',
		        height: 300,
		        width: '100%',
		        prompt: ': '
		    });*/
		// 1.5
		    // Terminal - Game stats (dynamic)
		    $("#terminal-charStats").terminal(function(command){
		    	if (command !== '') {
		    		if (command == 'stats') {

		    			this.echo(`Command ${command} displays characters stats.`);
		    		} else if (command == 'self') {

		    			this.echo(`Command ${command} displays info about your character.`);
		    		} else if (command == 'health') {
		    			`Command ${command} displays characters stats.`
		    		}else {

						this.echo('Unrecognised command.');
					}
		    	}
		    }, {
		        greetings: `Here you can check your characters stats and such!\n
Available commands are:
[[b;green;black]stats]
[[b;green;black]self]
[[b;green;black]health]`,
		        name: 'playArea',
		        height: '25vh',
		        width: '100%',
		        prompt: '>>> '
		    }, {
		    	// Has to be last, for everything to be read
		    	checkArity: false
			});

		// https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#masking-password
		// Works
		/*$("#terminal").terminal(function() {

			this.set_mask('-').read('pass: ').then(pass => this.echo("Your password is " + pass));
		});*/



	// 2. Code not working
		// 2.1
			// https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#prompt
			// 'term.set...' did not work. Nothing happended.

	// 3. To test
		// https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#reading-text-from-user
		// https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#key-shortcuts

	// 4. Functions and stuff
		function displayCommands(arrayCmds) {

			const displayCommandsTxt = [];
			displayCommandsTxt[0] = 'Available commands are:\n';
			for (let i = 0; i < arrayCmds.length; i++) {
				
				displayCommandsTxt[i+1] = `[[b;green;black]${arrayCmds[i]}] \n Type [[b;green;black]${arrayCmds[i]}Help] for command help.\n`;
			}
			return displayCommandsTxt;
		}
});