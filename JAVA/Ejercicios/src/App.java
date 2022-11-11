import condicionales.Condicionales;

public class App {
    public static void main(String[] args) throws Exception {
        Condicionales condicionales = new Condicionales("Jaqueline");
        String salida = condicionales.elSaludo();
        System.out.println(salida);
        String resultEje4 = condicionales.e4();
        System.out.println(resultEje4);
        System.out.println(condicionales.e5());

        
    }


}
