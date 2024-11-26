// 	Escribe una función que reciba dos números como parámetros y retorne su suma.

import java.util.Scanner;
//declaramos la variable
public class sumadedosnumeros {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //variable de los numeros enteros
        int E , F , Z;
        //pedimos al usuario que ingrese 2 numeros enteros
        System.out.println("Ingrese porfavor 2 numeros: ");
        //ingresar por teclado de ambos numeros
        E= scanner.nextInt();
        F= scanner.nextInt();
        // suma de los 2 numeros y que calcule el resultado
        Z= E +F;
        //imprimir por pantalla el resultado de los dos numeros
        System.out.println("la suma de los dos numeros ingresados es: " + Z);

        scanner.close();
    }
}