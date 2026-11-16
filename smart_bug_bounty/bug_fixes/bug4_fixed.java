
class Bug4Fixed {
    public static String getUserName(String[] users, int index) {
        if (users == null || index < 0 || index >= users.length) {
            return "Unknown User";
        }

        String name = users[index];

        if (name == null || name.isEmpty()) {
            return "Unknown User";
        }

        return name;
    }

    public static void main(String[] args) {
        String[] users = {"Alex", null, "Sarah", ""};

        System.out.println(getUserName(users, 0));
        System.out.println(getUserName(users, 1));
    }
}