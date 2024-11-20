import java.util.Scanner;

public class Puedesufragar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //Pedir ala persona su edad
        System.out.println("---¿Cual es su edad?porfavor ingresar---: ");
        int edad = scanner.nextInt();

        // verificar si es mayor de edad o no para poder sufragar

        if (edad>=18){
            System.out.println("Ya puedes votar!!! =) ");
        }   // si no tiene los 18 saldra este mensaje que aun no puede votar
            else {
                System.out.println("Oh aun no tienes la edad para poder votar =( ");
            }

            scanner.close();

        

    }
    
}
