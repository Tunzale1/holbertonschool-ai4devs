public class Bug4 {
    public static String getUserName(String[] users, int index) {
        String name = users[index];

        if (name.equals("")) {
            return "Unknown User";
        }

        return name;
    }

    public static void main(String[] args) {
        String[] users = {"Alex", null, "Sarah"};

        System.out.println(getUserName(users, 0));
        System.out.println(getUserName(users, 1));
    }
}