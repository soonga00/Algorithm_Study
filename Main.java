import java.util.Scanner;



public class Main {
    
    public static void main(String[] args) {
        int a, b;
        int cnt = 1;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        while(b != a)
        {
            if (b > a &&  b%2 == 0)
            {
                b /= 2;
                cnt++;
            }
            else if(b > a && b%10 == 1)
            {
                b /= 10;
                cnt++;
            }
            else {
                cnt = -1;
                break;
            }
        }
        System.out.println(cnt);

    }

}