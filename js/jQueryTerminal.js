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
						Terminal object -> Now able to send output to another terminal window!
							https://terminal.jcubic.pl/api_reference.php
			Q:	How to let users log in via the terminal?
					https://github.com/jcubic/jquery.terminal/wiki/Authentication
				Should other areas be rendered in the terminal as well?
				How to make sure the terminal keeps its size?
					Force a height in px, crude, vh didn't work
		Updated:
			2020-06-07
			2021-05-28 - 30
			2023-06-22
			2023-06-26
	*/

	// 1. Working code and semi-working code
		/*	https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#greetings
			greetings	works, however I'm getting error due not actually having the 'service.py' file
			prompt		works, but not together with greetings, probably because I need to pass multiple options inside an object
			2023-06-22: Simulated login, char create, explore and check stats functionality works.
				However available commands arrays doesn't seem to have updated, re-check if functions at the bottom are called properly and contain correct data.
			Add sounds & quite scary music
		*/	

		// 1.1 : Creates the terminal window
			$("#terminal-main").terminal({

				options: function(...args) {

		        	arrayCmds =	['options',
		        				'login',
		        				'logout'];

		        	let output = displayCommands( arrayCmds );

		        	// Prints out each command 
		        	for (let i = 0; i < output.length; i++) {
		        		this.echo(`${output[i]}`);
		        	}
		        },
		        login: function() {
		        	// After a successfull login add the first available command to the correct terminal
		        		// in the real game, the user will be able to retrive his/her char and continue the game or delete the char
		        	if (loggedIN == false) {

		        		this.echo(`Login feature not yet complete. This is a simulation.\nA new command is now available!\n`);
		        		//Updates loggedIN status
		        		loggedIN = true;

			        	let newCommand = `createChar`;
			        	availCmdsCmdArray = availableCmndsCommand(availCmdsCmdArray,newCommand);

			        	$('#terminal-commands').terminal().echo(`[[;white;black]Updating list...]`);
			        	let output = displayCommands( availCmdsCmdArray );
				        // Prints out each command 
				        for (let i = 0; i < output.length; i++) {
				        	$('#terminal-commands').terminal().echo(`${output[i]}`);
				        }
			        	$('#terminal-commands').terminal().echo(`On main terminal!\nProper word separation in development.\n`);
		        	} else {
		        		this.echo(`You are already logged-in.\n`);
		        	}
		        },
		        optionsHelp: function() {
		        	this.echo(`Type 'options' and hit enter!\n`);
		        },
		        loginHelp: function() {
		        	this.echo(`loginHelp\n`);
		        },
		        logout: function() {
		        	this.echo(`Game saved and you are logged out.\n`);
		        },
		        logoutHelp: function() {
		        	this.echo(`logoutHelp\n`);
		        },
		        createChar: function() {

		        	// Will be developed if I intend to create a demo-version of the game-idea.
		        	//const char = characterGen()

		        	if (loggedIN == true) {

		        		if ( charStatus == 'none') {
			        		this.echo(`Your character has been created!\nA new command is now available!\n`);
			        		// Char gen simulation
			        		charStatus = 'created';

			        		// Makes a new command available to the user
				        	let newCommand = `exploreSelf`;
			        		availCmdsCmdArray = availableCmndsCommand(availCmdsCmdArray,newCommand);
		        		
			        		$('#terminal-commands').terminal().echo(`[[;white;black]Updating list...]`);
			        		let output = displayCommands( availCmdsCmdArray );
					        // Prints out each command 
					        for (let i = 0; i < output.length; i++) {
					        	$('#terminal-commands').terminal().echo(`${output[i]}`);
					        }
			        		$('#terminal-commands').terminal().echo(`On main terminal!\nProper word separation in development.\n`);
			        	} else {
			        		this.echo(`Your character has already been created\n`);
			        	}
		        	} else {
		        		this.echo(`Unable to execute.\n`)
		        	}
		        },
		        exploreSelf: function() {

		        	if (loggedIN == true && charStatus == 'created') {

			        	this.echo(`You have just explored yourself.\nA new command is now available!\n`);

			        	exploreSelfStatus = 'explored';

			        	let newCommand = `stats`;
			        	availableCmndsCharStatsArray = availableCmndsCharStats(availableCmndsCharStatsArray, newCommand);
			        	//$('#terminal-charStats').terminal().echo(`New command(s) available:\n[[b;#66FF66;#282828]${availCmdsArray}]\n`);
			        	$('#terminal-charStats').terminal().echo(`[[;white;black]Updating list...]`);
		        		let output = displayCommands( availableCmndsCharStatsArray );
				        // Prints out each command 
				        for (let i = 0; i < output.length; i++) {
				        	$('#terminal-charStats').terminal().echo(`${output[i]}`);
				        }
			        	$('#terminal-charStats').terminal().echo(`On char stats terminal!\nProper word separation in development.\n`);
		        	} else if (exploreSelfStatus == 'explored') {
		        		$('#terminal-charStats').terminal().echo(`You have alrady explored yourself. Nothing new to report at this time.\n`);
		        	} else {
		        		this.echo(`Unable to execute.\n`);
		        	}
		        }
			}, {
		        greetings: `Welcome to NetSide! You'll find the repo @ [[!;i;black]https://github.com/JakobPapirov/NetSide]\n
[[b;#FFCC00;#282828]Game is in development.]\n
Type [[b;#66FF66;#282828]options] to view options:\n`,
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
			// Change this code to display available (discovered commands)
			$('#terminal-commands').terminal({
		        commandsList: function() {

		        	// availCmdsArray prints out the available commands.
		        	   // Which are populated from other #terminal-main
		        	let output = displayCommands( availCmdsCmdArray );

		        	this.echo(`[[;white;black]Listing commands...]`);
		        	// Prints out each command 
		        	for (let i = 0; i < output.length; i++) {
		        		this.echo(`${output[i]}`);
		        	}
		        },
		        commandsListHelp: function() {
		        	this.echo(`Type the command and hit enter.\n`);
		        },
		        createCharHelp: function() {
		        	if (loggedIN == true) {

		        		this.echo(`Type the command and hit enter.\n`);
		        	} else {
		        		this.echo(`Unable to execute.\n`);
		        	}
		        },
		        exploreSelfHelp: function() {
		        	if (charStatus == 'none') {

		        		this.echo(`Type the command and hit enter.\n`);
		        	} else {
		        		this.echo(`Unable to execute.\n`);
		        	}
		        }
		    }, {
		        greetings: "[[;blue;white]Game options terminal]\n",
		        name: 'gameCommands',
		        height: 300, // '25vh' doesn't work
		        width: '100%',
		        prompt: '>>> '
		    }, {
		    	// Has to be last, for everything to be read; allows for variable nr of inputs?
		    	checkArity: false
		    });

		// 1.5
		    // Terminal - Game stats (dynamic)
		    $("#terminal-charStats").terminal({
		    	
		    	commandsList: function() {

		        	// availCmdsArray prints out the available commands.
		        	   // Which are populated from other #terminal-main
		        	let output = displayCommands( availableCmndsCharStatsArray );

		        	this.echo(`[[;white;black]Listing commands...]`);
		        	// Prints out each command 
		        	for (let i = 0; i < output.length; i++) {
		        		this.echo(`${output[i]}`);
		        	}
		        },
		        commandsListHelp: function() {
		        	this.echo(`Type the command and hit enter.\n`);
		        },
		        stats: function() {
		        	
		        	if (exploreSelfStatus == 'explored') {

		        		let health = 100;
		        		this.echo(`[[;#FFCC00;#282828]Health:] [[;red;#282828]${health}]\n`);
		        	} else {

		        		this.echo(`Unable to execute.\n`);
		        	}
		        },
		        statsHelp: function() {

		        	if (exploreSelfStatus == 'explored') {

		        		this.echo(`Type the command and hit enter.\n`);
		        	} else {

		        		this.echo(`Unable to execute.\n`);
		        	}
		        },
		        somethingNewHelp: function() {
		        	this.echo(`Type the command and hit enter.\n`);
		        }
		    }, {
		        greetings: `Here you will be able to check your characters stats and such!\n`,
		        name: 'playArea',
		        height: 300,
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

		// 1.6
			// Terminal items
			$("#terminal-items").terminal(function(command){
				if (command !== '') {
		    		if (command == 'items') {

		    			this.echo(`Command ${command} displays your items.`);
		    		} else {

						this.echo('Unrecognised command.');
					}
		    	}
			}, {
				greetings: `[[;blue;white]Stay a while and listen ...]`,
				name: 'itemsArea',
		        height: 300,
		        width: '100%',
		        prompt: '>>> '
			}, {
		    	// Has to be last, for everything to be read
		    	checkArity: false
			});

	// 2. Code not working
		// 2.1
			// https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#prompt
			// 'term.set...' did not work. Nothing happended.

	// 3. To test
		// https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#reading-text-from-user
		// https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#key-shortcuts

	// 4. Functions and stuff
		// Sets initial statuses
		let loggedIN = false;
		let charStatus = 'none';
		let exploreSelfStatus = 'none';

		function displayCommands(arrayCmds) {

			// A worker-function that prepares an array to be printed out, by splitting up the individual list-items and prettifies it.
			const displayCommandsTxt = [];
			displayCommandsTxt[0] = 'Available commands are:\n';
			for (let i = 0; i < arrayCmds.length; i++) {
				
				displayCommandsTxt[i] = `Command: [[b;#00FF66;#282828]${arrayCmds[i]}] \nType [[b;#FFCC00;]${arrayCmds[i]}Help] for command help.\n`;
			}
			return displayCommandsTxt;
		}

		// Unused presently
		function characterGen() {

			const character = {
				 
			}
		}

		let availCmdsCmdArray =	['commandsList'];
		function availableCmndsCommand(availCmdsCmdArray, newCommand){
			
			// Commands in the commands-terminal
			availCmdsCmdArray.push(newCommand);

			return availCmdsCmdArray;
		}

		let availableCmndsCharStatsArray = ['commandsList'];
		function availableCmndsCharStats(availableCmndsCharStatsArray, newCommand){
			
			//Commands in the charStats-terminal
			availableCmndsCharStatsArray.push(newCommand);

			return availableCmndsCharStatsArray;
		}
});