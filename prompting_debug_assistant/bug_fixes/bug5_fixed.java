// Calculate the average exam score

public class Bug5 {

    public static double calculateAverage(int[] scores) {
        if (scores.length == 0) {
            throw new IllegalArgumentException("Scores cannot be empty");
        }

        int total = 0;

        for (int score : scores) {
            total += score;
        }

        double average = (double) total / scores.length;

        return average;
    }

    public static void main(String[] args) {
        int[] scores = {75, 80, 86};

        double result = calculateAverage(scores);

        assert Math.abs(result - 80.3333333333) < 0.000001;
        assert calculateAverage(new int[]{10, 20}) == 15.0;

        System.out.println("Bug 5 fixed successfully!");
        System.out.println("Average score: " + result);
    }
}