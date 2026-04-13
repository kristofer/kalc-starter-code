class Kalc {

    static void main(String[] args) {
        System.out.println("Welcome to Kalc");

        boolean done = false;
        String input = "";
        while (!done) {
            input = System.console().readLine();
            if (input.equals("exit")) {
                done = true;
            }
        }
        System.out.println("Goodbye!");
    }
}
