import java.util.Scanner;

public class mayordetres {
    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);

        System.out.println("ingresar el primer numero: ");
        System.out.println("ingresar el segundo  numero: ");
        System.out.println("ingresar el tercer numero: ");
        System.out.println("----------------------------------");
        int nume1=scanner.nextInt();
        int nume2=scanner.nextInt();
        int nume3=scanner.nextInt();

        int numeromayor = nume1;

        if (nume2>numeromayor){
            numeromayor=nume2;
        }
        if (nume3 > numeromayor) {
            numeromayor = nume3;

    }
    System.out.println("el numero mayor de los 3 es: "+numeromayor);
    scanner.close();
}
}