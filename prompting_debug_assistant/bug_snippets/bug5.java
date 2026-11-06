// Calculate the average exam score

public class Bug5 {

    public static double calculateAverage(int[] scores) {
        int total = 0;

        for (int score : scores) {
            total += score;
        }

        int average = total / scores.length;

        return average;
    }

    public static void main(String[] args) {
        int[] scores = {75, 80, 86};

        System.out.println(
            "Average score: " + calculateAverage(scores)
        );
    }
}