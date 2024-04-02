CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);




CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);





CREATE TABLE registrations (
    registration_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);



SELECT c.course_name, COUNT(r.student_id) AS student_count
FROM courses c
LEFT JOIN registrations r ON c.course_id = r.course_id
GROUP BY c.course_name;

