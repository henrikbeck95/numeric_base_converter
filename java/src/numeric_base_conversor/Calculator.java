package numeric_base_conversor;

import java.util.ArrayList;
import java.util.List;

public class Calculator {
	private static boolean DEBUG;
	private static int NUMERIC_BASE_CURRENT;
	private static int NUMERIC_BASE_TARGET;
	private static int NUMBER_VALUE_CURRENT;
	private static final String MESSAGE_ERROR = "Ainda não foi implementado";

	public Calculator(boolean debug, int numericBaseCurrent, int numericBasetarget, Object numberValueCurrent) {
		Calculator.DEBUG = debug;
		Calculator.NUMERIC_BASE_CURRENT = numericBaseCurrent;
		Calculator.NUMERIC_BASE_TARGET = numericBasetarget;
		
		//Convert object value to integer
		if(numberValueCurrent instanceof Integer) {
			Calculator.NUMBER_VALUE_CURRENT = (int) numberValueCurrent;
		}else {
			List <Object> ArrayListObject = new ArrayList<Object>();
			ArrayListObject = Utils.fixHexaReplaceStringToInteger(numberValueCurrent);
			
			//Calculator.NUMBER_VALUE_CURRENT = numberValueCurrent;
			//System.out.println("Resultado na base 10: " + NUMBER_VALUE_CURRENT + "\n");
			Calculator.NUMBER_VALUE_CURRENT = convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListObject);
			Calculator.NUMERIC_BASE_CURRENT = 10; //This must be set right after this.NUMBER_VALUE_CURRENT value
		}
		
		long result = calculateNumberValueTarget(Calculator.NUMBER_VALUE_CURRENT);
		Utils.printResult(Calculator.NUMERIC_BASE_CURRENT, Calculator.NUMERIC_BASE_TARGET, Calculator.NUMBER_VALUE_CURRENT, result);
	}

	private static long calculateNumberValueTarget(int NUMBER_VALUE_CURRENT) {
		List <Object> ArrayListNumberValueSplited = new ArrayList<Object>();
		ArrayListNumberValueSplited = Utils.convertNumericValueToArrayList(NUMBER_VALUE_CURRENT);

		/*
		if(NUMERIC_BASE_CURRENT > NUMERIC_BASE_TARGET) {
			return convertBaseMethodDivider(ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT < NUMERIC_BASE_TARGET) {
			return convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
		}else {
			return -1;
		}
		*/
		
		//Calculate process workflow
		if(NUMERIC_BASE_CURRENT == NUMERIC_BASE_TARGET){
			return NUMBER_VALUE_CURRENT;
		}else if(NUMERIC_BASE_CURRENT == 2 && NUMERIC_BASE_TARGET == 8) {
			long decimal = convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
			return convertBaseMethodDivider(decimal, 8, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 2 && NUMERIC_BASE_TARGET == 10) {
			return convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 2 && NUMERIC_BASE_TARGET == 16) {
			long decimal = convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
			return convertBaseMethodDivider(decimal, 16, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 8 && NUMERIC_BASE_TARGET == 2) {
			return convertBaseMethodDivider(NUMBER_VALUE_CURRENT, NUMERIC_BASE_TARGET, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 8 && NUMERIC_BASE_TARGET == 10) {
			return convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 8 && NUMERIC_BASE_TARGET == 16) {
			long decimal = convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
			return convertBaseMethodDivider(decimal, 16, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 10 && NUMERIC_BASE_TARGET == 2) {
			return convertBaseMethodDivider(NUMBER_VALUE_CURRENT, NUMERIC_BASE_TARGET, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 10 && NUMERIC_BASE_TARGET == 8) {
			return convertBaseMethodDivider(NUMBER_VALUE_CURRENT, NUMERIC_BASE_TARGET, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 10 && NUMERIC_BASE_TARGET == 16) {
			long decimal = convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
			return convertBaseMethodDivider(decimal, 16, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 16 && NUMERIC_BASE_TARGET == 2) {
			long decimal = convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
			return convertBaseMethodDivider(decimal, NUMERIC_BASE_TARGET, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 16 && NUMERIC_BASE_TARGET == 8) {
			long decimal = convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
			return convertBaseMethodDivider(decimal, NUMERIC_BASE_TARGET, ArrayListNumberValueSplited);
		}else if(NUMERIC_BASE_CURRENT == 16 && NUMERIC_BASE_TARGET == 10) {
			return convertBaseMethodMultiplier(NUMERIC_BASE_CURRENT, ArrayListNumberValueSplited);
		}else {
			System.err.println(MESSAGE_ERROR);
			return -1;			
		}
	}

	private static int convertBaseMethodMultiplier(int baseValue, List<Object> ArrayListObject) {
		List<Integer> ArrayListInteger = Utils.convertArrayListToInteger(ArrayListObject);
		
		int aux = 0;
		int somatario = 0;
		
		if(DEBUG) {
			System.out.println("\nPasso a passo da resolução do problema:");
		}

		//Sum all list indexes
		for (int i = 0; i < ArrayListInteger.size(); i++) {
			aux = (int) (Integer.parseInt(ArrayListInteger.get(i).toString()) * Math.pow(baseValue, i));
			somatario += aux;

			//Describing result process
			if(DEBUG) {
				System.out.println(Integer.parseInt(ArrayListInteger.get(i).toString()) + " * " + baseValue + "^" + i + " = " + aux);
			}
		}
		
		if(DEBUG) {
			System.out.println("");
		}
		
		return somatario;
	}
	
    private static long convertBaseMethodDivider(long numberValue, int baseTarget, List<Object> ArrayListObject) {
        List <Long> ArrayListRests = new ArrayList<Long>();
        
        long divisionRest = 0;
		long aux = 0;

		while(numberValue > 0) {
			divisionRest = numberValue % baseTarget;
			aux = numberValue / baseTarget;
			
			//Describing result process
			if(DEBUG) {
				System.out.println(numberValue + " / " + baseTarget + " = " + aux + "\t&&\tResto = " + divisionRest);
			}
			
			ArrayListRests.add(divisionRest);
			numberValue = aux;
		}
		
		if(DEBUG) {
			System.out.println("\nBinary = " + ArrayListRests.toString() + "\n");
		}
		
		//Merge ArrayList into one single number
		String numberValueBinaryString = "";

		for(int i = ArrayListRests.size() - 1; i >= 0; i--) {
			numberValueBinaryString += ArrayListRests.get(i).toString();
			
			if(DEBUG) {
				System.out.println(numberValueBinaryString);
			}
		}
		
		return Long.parseLong(numberValueBinaryString);
	}
}