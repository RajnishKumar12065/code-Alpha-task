#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define student structure
struct Student {
    int rollNo;
    char name[50];
    int age;
    float marks;
};

// Function prototypes
void addStudent();
void displayStudents();
void searchStudent();
void updateStudent();
void deleteStudent();

// File name
const char *filename = "student.dat";

int main() {
    int choice;
    do {
        printf("\n===== Student Management System =====\n");
        printf("1. Add Student\n");
        printf("2. Display All Students\n");
        printf("3. Search Student by Roll No\n");
        printf("4. Update Student\n");
        printf("5. Delete Student\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1: addStudent(); break;
            case 2: displayStudents(); break;
            case 3: searchStudent(); break;
            case 4: updateStudent(); break;
            case 5: deleteStudent(); break;
            case 6: printf("Exiting program...\n"); break;
            default: printf("Invalid choice! Try again.\n");
        }
    } while(choice != 6);

    return 0;
}

// Function to add a student
void addStudent() {
    FILE *fp = fopen(filename, "ab");
    if(fp == NULL) {
        printf("Error opening file!\n");
        return;
    }

    struct Student s;
    printf("Enter Roll No: ");
    scanf("%d", &s.rollNo);
    printf("Enter Name: ");
    getchar(); // clear buffer
    fgets(s.name, sizeof(s.name), stdin);
    s.name[strcspn(s.name, "\n")] = '\0'; // remove newline
    printf("Enter Age: ");
    scanf("%d", &s.age);
    printf("Enter Marks: ");
    scanf("%f", &s.marks);

    fwrite(&s, sizeof(s), 1, fp);
    fclose(fp);
    printf("Student record added successfully!\n");
}

// Function to display all students
void displayStudents() {
    FILE *fp = fopen(filename, "rb");
    if(fp == NULL) {
        printf("No records found!\n");
        return;
    }

    struct Student s;
    printf("\n--- Student Records ---\n");
    while(fread(&s, sizeof(s), 1, fp)) {
        printf("Roll No: %d\nName: %s\nAge: %d\nMarks: %.2f\n\n",
               s.rollNo, s.name, s.age, s.marks);
    }
    fclose(fp);
}

// Function to search student by Roll No
void searchStudent() {
    FILE *fp = fopen(filename, "rb");
    if(fp == NULL) {
        printf("No records found!\n");
        return;
    }

    int roll, found = 0;
    printf("Enter Roll No to search: ");
    scanf("%d", &roll);

    struct Student s;
    while(fread(&s, sizeof(s), 1, fp)) {
        if(s.rollNo == roll) {
            printf("Record Found:\nRoll No: %d\nName: %s\nAge: %d\nMarks: %.2f\n",
                   s.rollNo, s.name, s.age, s.marks);
            found = 1;
            break;
        }
    }
    if(!found) printf("Student with Roll No %d not found!\n", roll);

    fclose(fp);
}

// Function to update student record
void updateStudent() {
    FILE *fp = fopen(filename, "rb+");
    if(fp == NULL) {
        printf("No records found!\n");
        return;
    }

    int roll, found = 0;
    printf("Enter Roll No to update: ");
    scanf("%d", &roll);

    struct Student s;
    long pos;
    while(fread(&s, sizeof(s), 1, fp)) {
        if(s.rollNo == roll) {
            printf("Enter new Name: ");
            getchar();
            fgets(s.name, sizeof(s.name), stdin);
            s.name[strcspn(s.name, "\n")] = '\0';
            printf("Enter new Age: ");
            scanf("%d", &s.age);
            printf("Enter new Marks: ");
            scanf("%f", &s.marks);

            pos = ftell(fp) - sizeof(s);
            fseek(fp, pos, SEEK_SET);
            fwrite(&s, sizeof(s), 1, fp);
            printf("Record updated successfully!\n");
            found = 1;
            break;
        }
    }
    if(!found) printf("Student with Roll No %d not found!\n", roll);

    fclose(fp);
}

// Function to delete student record
void deleteStudent() {
    FILE *fp = fopen(filename, "rb");
    if(fp == NULL) {
        printf("No records found!\n");
        return;
    }

    FILE *temp = fopen("temp.dat", "wb");
    if(temp == NULL) {
        printf("Error opening temp file!\n");
        fclose(fp);
        return;
    }

    int roll, found = 0;
    printf("Enter Roll No to delete: ");
    scanf("%d", &roll);

    struct Student s;
    while(fread(&s, sizeof(s), 1, fp)) {
        if(s.rollNo != roll) {
            fwrite(&s, sizeof(s), 1, temp);
        } else {
            found = 1;
        }
    }

    fclose(fp);
    fclose(temp);

    remove(filename);
    rename("temp.dat", filename);

    if(found)
        printf("Record deleted successfully!\n");
    else
        printf("Student with Roll No %d not found!\n", roll);
}
