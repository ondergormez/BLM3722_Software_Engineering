
## Kısıtlamalar
* Tool içi dolu ok çizdiği için türetmelerde kullanılan okların içi dolu olarak gösterilmiştir.
* Tool otomatik olarak çizdiği için görsellerde karmaşık görünüm ortaya çıkabiliyor.

TODO: Dışardan erişilemeyenleri "-" ile ifade et.
TODO: Variable lar ile method lar arasına boşluk koy
TODO: 2 class definition arasına boşluk koy

```mermaid
classDiagram
    Course o-- Student  : Aggregation
    InformationSystem "1" --> "*" SchoolBranch
    SchoolBranch *-- Classroom 
    Classroom *-- Course
    Person <|-- Student : Inheritance
    Person <|-- Worker : Inheritance
    Worker <|-- Teacher : Inheritance
    Worker <|-- Registrar : Inheritance
    Worker <|-- SystemAdmin : Inheritance
    Course o-- Teacher  : Aggregation
    InformationSystem "1" --> "*" Person

    class Person{
      
    }

    class InformationSystem{

    }

    class Student{
    }

    class Worker{
    }
    
    class Teacher{
    }

    class Registrar{
    }

    class SchoolBranch{
    }

    class Course{
    }
```
TODO: 
BTool böyle okun içi dolu
classA --|> classB : Inheritance
classC --* classD : Composition
classE --o classF : Aggregation
classG --> classH : Association
classI -- classJ : Link(Solid)
classK ..> classL : Dependency
classM ..|> classN : Realization
classO .. classP : Link(Dashed)

```mermaid
classDiagram
    Person <|-- Student : Inheritance
    Person <|-- Worker : Inheritance
    Worker <|-- Teacher : Inheritance
    Worker <|-- Registrar : Inheritance
    Worker <|-- SystemAdmin: Interitance

    class Person{
    -p_name: String
    -p_surname: String
    -p_age: int
    -p_gender: String
    -p_mobilephone: String
    -p_phone: String
    -p_email: String
    -p_address: String
    +Person(String name, String surname, String mobilephone, String phone, String email, int age, String gender, String address)
    +setName(String newName) void
    +getName() String
    }


    class Student{
      -s_courses :vector~String~ 
      -s_courseLevel :vector~String~ 
      -s_paymentInfos :String 
      +newStudent() Student
      +deleteStudent()
      +addToCourse(course: Course) bool
      +deleteFromCourse(course: Course) bool
    }

    class Worker{
      -w_workStartDate :String 
      -w_workEndDate :String 
      -w_isActiveWorker :bool 
      -w_salary : int 
      -w_role : String
      +updateSalary(newSalary: double) void
      +newWorker() Worker
      +deleteWorker(worker: Worker) bool
    }
    
    class Teacher{
      -t_languages : vector~String~ 
      -t_classBranches : vector~SchoolBranch~ 
      -t_availableDays : String 
      -t_availableHours : String 
      +newTeacher()  Teacher
    }

    class Registrar{
      -userName :String
      -password :String
      +newRegistrar() Registrar
      +loginToSystem(userName: String, password: String) bool
      +registerStudentForClass(student: Student, course: Course) bool 
      +registerPayment(student: Student, paymentInfo: student.paymentInfos)
    }

    class SystemAdmin{
      -userName :String
      -password :String
      +newSystemAdmin() SystemAdmin
      +loginToSystem(userName: String, password: String) bool
    }


```

* Yukarıda detayı verilen sınıfların detayları tekrar yazılmamıştır.

```mermaid
classDiagram
    SchoolBranch *-- Classroom 
    Classroom *-- Course
    class SchoolBranch{
        -sc_name : String
        -sc_address : String
        -sc_publicTransport : String
        -sc_privateTransport : String
        -sc_socialBenefits : vector~String~ 
        -sc_allClasses : vector~ClassRoom~ 
        +showClassrooms() : vector~ClassRoom~
        +addNewClassroom(classroom: Classroom) bool
        +deleteClassroom(classroom: Classroom) bool
    }

    class Classroom{
        -cl_name : String
        -cl_capacity : int
        -courseList : vector~Course~
        +showCourses() : vector~Course~
        +addNewCourse(course: Course) bool
        +deleteCourse(course: Course) bool       
    }

    class Course{
        -co_name : String
        -co_capacity : int
        -co_registeredStudentCount : int
        -co_level : String
        -co_course_classroom : Classroom
        -co_studentList : vector~Student~
        -co_teacher : Teacher
        -co_date : Date
        +setName(newCourseName: String) void
        +getName() String
        +showStudents()  vector~Student~
    }
```

```mermaid
classDiagram
    class InformationSystem{
      -i_total_users : int
      -i_total_branches : int
      -i_worker_list vector~Worker~
      -i_student_list vector~Student~
      +addNewWorker()
      +deleteWorker()
      +addNewStudent()
      +deleteStudent()
      +addNewBranch()
      +deleteBranch()
      +addNewClassroom()
      +deleteClassroom()
      +addNewCourse()
      +deleteCourse()
      +registerPayment()
      +showWorkers() vector~Worker~
    }
```


## Kaynaklar
[Class Diagram](https://mermaid-js.github.io/mermaid/#/classDiagram)
