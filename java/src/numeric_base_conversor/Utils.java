package numeric_base_conversor;

import java.util.ArrayList;
import java.util.List;

public class Utils {
	//Define color constants
	public static final String COLOR_BLACK = "\u001B[30m";
	public static final String COLOR_BLUE = "\u001B[34m";
	public static final String COLOR_CYAN = "\u001B[36m";
	public static final String COLOR_GREEN = "\u001B[32m";
	public static final String COLOR_PURPLE = "\u001B[35m";
	public static final String COLOR_RED = "\u001B[31m";
	public static final String COLOR_YELLOW = "\u001B[33m";
	public static final String COLOR_WHITE = "\u001B[37m";
	public static final String COLOR_RESET = "\u001B[0m";
	
	public static List <Object> convertNumericValueToArrayList(Object numberValue) {
		List <Object> ArrayList = new ArrayList<Object>();
		
		String str = numberValue.toString();
		String[] arr = str.split("");
		
		//Split each digit to a different index
		//for(int i = 0; i < arr.length; i++) {//Start from first element
		for(int i = arr.length - 1; i >= 0; i--) { //Start from last element
			ArrayList.add(arr[i]);
		}

		return ArrayList;
	}

	public static List <Integer> convertArrayListToInteger(List<Object> ArrayListObject) {
		List <Integer> ArrayListInteger = new ArrayList<Integer>();
		
		for(int i = 0; i < ArrayListObject.size(); i++) {
			switch (ArrayListObject.get(i).toString()) {
				case "A": ArrayListInteger.add(10); break;
				case "B": ArrayListInteger.add(11); break;
				case "C": ArrayListInteger.add(12); break;
				case "D": ArrayListInteger.add(13); break;
				case "E": ArrayListInteger.add(14); break;
				case "F": ArrayListInteger.add(15); break;
				default:  ArrayListInteger.add(Integer.parseInt(ArrayListObject.get(i).toString()));
			}
		}
		
		return ArrayListInteger;
	}
	
	public static List <Object> convertArrayListToObject(List<Integer> ArrayListInteger){
		List <Object> ArrayListObject = new ArrayList<Object>();
		
		for(int i = 0; i < ArrayListInteger.size(); i++) {
			ArrayListObject.add((String) ArrayListInteger.get(i).toString());
		}
		
		return ArrayListObject;
	}
	
	public static List <String> convertArrayListToString(List<Object> ArrayListObject) {
		List <String> ArrayListString = new ArrayList<String>();
		
		for(int i = 0; i < ArrayListObject.size(); i++) {
			switch (Integer.parseInt(ArrayListObject.get(i).toString())) {
				case 10: ArrayListString.add("10"); break;
				case 11: ArrayListString.add("11"); break;
				case 12: ArrayListString.add("12"); break;
				case 13: ArrayListString.add("13"); break;
				case 14: ArrayListString.add("14"); break;
				case 15: ArrayListString.add("15"); break;
				default: ArrayListString.add(ArrayListObject.get(i).toString());
			}
		}
		
		return ArrayListString;
	}
	
	public static List <Object> fixHexaReplaceStringToInteger(Object numberValueCurrent){
		System.out.println("Número informado: " + numberValueCurrent.toString());
		
		List <Object> ArrayListAuxObject = new ArrayList<Object>();
		ArrayListAuxObject = Utils.convertNumericValueToArrayList(numberValueCurrent);
		//System.out.println("ArrayListAuxObject: " + ArrayListAuxObject.toString());
		
		List <Integer> ArrayListAuxInteger = new ArrayList<Integer>();
		ArrayListAuxInteger = Utils.convertArrayListToInteger(ArrayListAuxObject);
		//System.out.println("ArrayListAuxInteger: " + ArrayListAuxInteger.toString());
		
		
		List <Object> ArrayListAuxObject2 = new ArrayList<Object>();
		ArrayListAuxObject2 = Utils.convertArrayListToObject(ArrayListAuxInteger);
		//System.out.println("ArrayListAuxObject2: " + ArrayListAuxObject2.toString());
		//System.out.println((ArrayListAuxObject2.get(0)).getClass().getName());
		
		return ArrayListAuxObject2;
	}
	
	public static void printResult(int baseCurrent, int baseTarget, int valueCurrent, long result) {
		System.out.println("\nValores informados:");
		System.out.println("Base numérica atual:\t" + baseCurrent);
		System.out.println("Base numérica desejada:\t" + baseTarget);
		System.out.println("Resultado:\t\t" + "(" + valueCurrent + ")" + baseCurrent + " <=> " + "("
				+ result + ")" + baseTarget);
		printSeparor();
	}
	
	public static void printSeparor() {
		System.out.println(COLOR_RED + "-------------------------***-------------------------" + COLOR_RESET);		
	}
}