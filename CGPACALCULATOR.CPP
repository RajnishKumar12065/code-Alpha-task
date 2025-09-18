#include <stdio.h>

// Function to convert grade into grade points
float gradeToPoint(char grade) {
    switch(grade) {
        case 'A': return 10.0;
        case 'B': return 8.0;
        case 'C': return 6.0;
        case 'D': return 4.0;
        case 'E': return 2.0;
        case 'F': return 0.0;
        default: return -1.0;
    }
}

int main() {
    int n, i;
    char grade;
    int credit;
    float totalCredits = 0, totalGradePoints = 0;
    
    printf("Enter number of courses: ");
    scanf("%d", &n);

    for(i = 1; i <= n; i++) {
        printf("\nCourse %d:\n", i);
        printf("Enter grade (A-F): ");
        scanf(" %c", &grade); 
        printf("Enter credit hours: ");
        scanf("%d", &credit);

        float points = gradeToPoint(grade);

        if(points < 0) {
            printf("Invalid grade entered! Try again.\n");
            i--; 
            continue;
        }

        totalCredits += credit;
        totalGradePoints += points * credit;

        printf("Course %d -> Grade: %c, Credit: %d, Points: %.1f\n", i, grade, credit, points);
    }

    float cgpa = totalGradePoints / totalCredits;

    printf("\nTotal Credits = %.1f", totalCredits);
    printf("\nTotal Grade Points = %.1f", totalGradePoints);
    printf("\nFinal CGPA = %.2f\n", cgpa);

    return 0;
}
