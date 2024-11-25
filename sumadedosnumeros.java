// 	Escribe una función que reciba dos números como parámetros y retorne su suma.

import java.util.Scanner;
//declaramos la variable
public class sumadedosnumeros {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //variable
        int E , F , Z;
        System.out.println("Ingrese porfavor 2 numeros: ");
        E= scanner.nextInt();
        F= scanner.nextInt();
        Z= E +F;
        System.out.println("la suma de los dos numeros ingresados es: " + Z);

        scanner.close();
    }
}