import java.util.Scanner;

public class descuentodetienda {
    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);
        //pedir la cantidad del dinero al cliente
        System.out.println("----Ingresar dinero en numero entero-----");
        System.out.println("--Ingresar el monto del dinero gastado: $--");
        double cantidad=scanner.nextDouble();
        
        //Hacer los calculos si aplica descuento o no

        if (cantidad>100){
            double descuento = cantidad * 0.20;
            double cantidadfinal=cantidad - descuento;
            System.out.println("Cantidad final con el descuento :$ "+ cantidadfinal);
            //en caso contrario que sea menor a 100 no dara descuento
        } else {
            System.out.println("Cantidad final no aplica descuento $:$ " + cantidad);
        }

        scanner.close();

    }
    
}
