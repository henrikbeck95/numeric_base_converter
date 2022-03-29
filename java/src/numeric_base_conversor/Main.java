package numeric_base_conversor;

import java.util.Scanner;

public class Main {
	static final Scanner SCAN = new Scanner(System.in);
	
	public static void main(String[] args) {
		System.out.println("Conversor de bases numéricas");
		System.out.println("----------------------------");
		System.out.println("Números hexadecimais precisam ser maiúsculos");
		Utils.printSeparor();
		
		//interactiveFromCommandLineInterface(args);
		//interactiveFromKeyboard();
		interactiveFromObjectInstance();
	}
	
	private static void interactiveFromCommandLineInterface(String[] arguments) {
		boolean debug = Boolean.parseBoolean(arguments[0]);
		int numericBaseCurrent = Integer.parseInt(arguments[1]);
		int numericBasetarget = Integer.parseInt(arguments[2]);
		int numberValueCurrent = Integer.parseInt(arguments[3]);
		
		Calculator calculator = new Calculator(debug, numericBaseCurrent, numericBasetarget, numberValueCurrent);
	}
	
	private static void interactiveFromKeyboard() {
		System.out.println("Deseja ver o passo a passo da resolução do problema (y/N): ");
		char answer = SCAN.next().charAt(0); //c = entrada.next().charAt(0);
		
		boolean DEBUG;
		switch(answer) {
			case 'y': DEBUG = true; break;
			case 'n': DEBUG = false; break;
			default: DEBUG = true;
		}
		
		System.out.println("Informe o valor da base numérica atual: ");
		int numericBaseCurrent = SCAN.nextInt();
		
		System.out.println("Informe o valor da base desejada: ");
		int numericBasetarget = SCAN.nextInt();
		
		System.out.println("Informe o valor do número a ser convertido: ");
		String numberValueCurrentTemp = SCAN.next();
		Object numberValueCurrent = numberValueCurrentTemp;
		
		Calculator calculator = new Calculator(DEBUG, numericBaseCurrent, numericBasetarget, numberValueCurrent);
	}

	private static void interactiveFromObjectInstance() {
		//final boolean DEBUG = false;
		final boolean DEBUG = true;
		
		/**/
		Calculator calculator00 = new Calculator(DEBUG, 8, 8, 73); 			//73
		
		Calculator calculator01 = new Calculator(DEBUG, 2, 8, 1001001);		//111
		Calculator calculator02 = new Calculator(DEBUG, 2, 10, 1001001);	//73
		Calculator calculator03 = new Calculator(DEBUG, 2, 16, 1001001);	//49
		
		Calculator calculator04 = new Calculator(DEBUG, 8, 2, 207);			//11001111
		Calculator calculator05 = new Calculator(DEBUG, 8, 10, 207);		//135
		Calculator calculator06 = new Calculator(DEBUG, 8, 16, 207);		//87
		
		Calculator calculator07 = new Calculator(DEBUG, 10, 2, 207);		//11001111
		Calculator calculator08 = new Calculator(DEBUG, 10, 8, 99);			//143
		Calculator calculator09 = new Calculator(DEBUG, 10, 16, 99);		//63
		
		Calculator calculator10 = new Calculator(DEBUG, 16, 2, "1FA");		//111111010
		Calculator calculator11 = new Calculator(DEBUG, 16, 8, "1FA");		//772
		Calculator calculator12 = new Calculator(DEBUG, 16, 10, "1FA");		//506
		
		Calculator calculator14 = new Calculator(DEBUG, 16, 2, "ABC");		//101010111100
		Calculator calculator15 = new Calculator(DEBUG, 16, 8, "ABC");		//5274
		Calculator calculator16 = new Calculator(DEBUG, 16, 10, "ABC");		//2748

		Calculator calculator17 = new Calculator(DEBUG, 16, 2, 20);			//100000
		Calculator calculator18 = new Calculator(DEBUG, 16, 8, 20);			//40
		Calculator calculator19 = new Calculator(DEBUG, 16, 10, 20);		//32
		/**/
		
	}
}