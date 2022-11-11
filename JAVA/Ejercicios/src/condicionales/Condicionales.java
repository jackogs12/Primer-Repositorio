package condicionales;
import java.util.Scanner;

public class Condicionales{
    //variables de instancia
    private static Scanner sc = new Scanner(System.in);
    //!constructor es el método se ejecutara al crear un objeto.

    // constructor
    public Condicionales(String nombre) {
        //método que se ejecuta cuando creo un objeto con new objetc();
        System.out.println("Hola "+nombre+" desde el constructor de condiconales");
        //Inicializar las variables
    }

    public String elSaludo(){
        //entrada
        System.out.println("Ingresa tu edad: ");
        int edad = sc.nextInt();
        sc.close();
        //verificar si es mayor de edad
        if(edad>=18){ //edad>17
            return "Eres mayor de edad"; // sentencia mayor de edad
        } else{
            return"Eres menor de edad"; // sentencia menor de edad
        }
    }

    /*Ejercicio 4. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar. */
/**
 * 
 * @return si el número ingresado es par o impar.
 */
public String e4(){
    //entrada
    System.out.print("Ingresa un número entero");
    int numero = sc.nextInt();
    if(numero % 2 == 0){
        return "El "+numero+ "es par";

    }else{
        return "El "+numero+ "es impar";

    }
}

/*Ejercicio 5. Para pagar un determinado impuesto se debe ser mayor de 16 años y 
tener unos ingresos iguales o superiores a $5000 mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y 
 muestre por pantalla si el usuario tiene que pagar o no. */
/**
 * 
 * @return Si el usuario debe pagar o no imouestos.
 */


public static String e5(){
    System.out.println("Ingresa tu edad");
    int edad = sc.nextInt();
    System.out.println("Ingresa tus ingresos mensuales");
    double ingreso = sc.nextDouble();
    if(edad > 18 && ingreso > 5000){
        return "Debes pagar Impuestos";

    }else{
        return "No pagas impuestos";
    }
}

/*Ejercicio 6. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde.*/

public static String e6();{
System.out.println("Ingresa tu nombre");
String nombre = sc.nextLine();
System.out.println("Ingresa tu sexo M/H");
char sexo = sc.next().charAt();
if((sexo =='M' && nombre[0] < 'M')||(sexo == 'H' && nombre [0] > 'N')){
    return "Perteneces al grupo A";

}else{
    return "Perteneces al grupo B";
}

}



}   

