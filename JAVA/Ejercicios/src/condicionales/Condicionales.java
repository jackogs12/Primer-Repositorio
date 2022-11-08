package condicionales;
import java.util.Scanner;

public class Condicionales{
    //variables de instancia
    private static Scanner sc = new Scanner(System.in);
    //!constructor es el método se ejecutara al crear un objeto.

    // constructor
    public Condicionales(String nombre) {
        
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


public String e3Div(){
    System.out.println("Ingresa el primer número: ");
    int n1 = sc.nextInt();
    System.out.println("Ingresa el segundo número");
    int n2 = sc.nextInt();
    sc.close();
    // Valida si el divisor es cero retorna error
    int div = 0;

    if(n1 == 0){
        return "Error división indefinida";
    }else{
        div = (n1/n2);
        System.out.println("El resultado de la suma es: " + div +"");
    }

    



}
    
}    

