import java.util.Scanner;

public class mayordetres {
    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);
        // pedimos el ingreso de los tres numero
        System.out.println("ingresar el primer numero: ");
        System.out.println("ingresar el segundo  numero: ");
        System.out.println("ingresar el tercer numero: ");
        System.out.println("----------------------------------");
        // los 3 numeros puestos por el usuario
        int nume1=scanner.nextInt();
        int nume2=scanner.nextInt();
        int nume3=scanner.nextInt();
        //Calcular cual es el numero mayor entre los 3
        int numeromayor = nume1;

        if (nume2>numeromayor){
            numeromayor=nume2;
        }
        if (nume3 > numeromayor) {
            numeromayor = nume3;

    }
    //mostrar por pantalla el numero mayor 
    System.out.println("el numero mayor de los 3 es: "+numeromayor);
    scanner.close();
}
}