public class char_alloc_n_write_m {
    public static void main(String[] args) {
        if (args.length < 1)
            System.exit(1);
        int n = Integer.valueOf(args[0]);

        if (n < 0)
            System.exit(2);
        System.out.println(n);

        char[] p = new char[n];
        System.out.println("alloc done");

        if (args.length == 2) {
            int m = Integer.valueOf(args[1]);

            if (m < 0 || m > n)
                System.exit(3);
            System.out.println(m);

            for (int i = 0; i < m; i++)
                p[i] = 'a';
            System.out.println("write done");
        }
    }
}
