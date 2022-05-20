
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
    -name: String
    -surname: String
    -birthdate: Date
    -gender: String
    -mobile_phone: String
    -phone: String
    -email: String
    -address: String
    -syst_priv : bool
    +new_person(name: String , surname: String, mobile_phone: String, phone: String , email: String, age: int, gender: String, address: String)
    +set_mobile_phone(new_mobile_phone: String ) void
    +get_contact_info() String
    }
```

```mermaid
classDiagram
    class Student{
      -courses :vector~String~ 
      -course_level :vector~String~ 
      -payment_infos :String 
      +new_student(person: Person, course_list: vector~String~, course_levels: vector~String~, payment_infos: String) Student
      +get_course_list() : vector~String~
      +display_student() void
      +delete_student() bool
    }
```

```mermaid
classDiagram
    class Worker{
      -start_date : String 
      -end_date : String 
      -active_worker : bool 
      -salary : int 
      -role : String
      +new_worker(person: Person, start_date: String, end_date: String, active_worker : bool, salary: int,  role: String) Worker
      +delete_worker() bool
      +update_salary(new_salary: double) void
      +end_contract() void
    }
```

```mermaid
classDiagram    
    class Teacher{
      -languages : vector~String~ 
      -available_branches : vector~SchoolBranch~ 
      -available_days : String 
      -available_hours : String
      -available_times : Dictionary
      +new_teacher(person: Person, languages : vector~String~, available_branches : vector~SchoolBranch~, available_days : String, available_hours : String)  Teacher
     +delete_teacher() bool
     +set_available_times()
     +get_available_times()
     +find_teacher(teacher_list: vector~Teacher~, day: String)
    }
```

```mermaid
classDiagram
    class Registrar{
      -user_name :String
      -password :String
      +new_registrar() Registrar
      +delete_registrar() bool
      +log_in(syst_priv : bool, userName: String, password: String) bool
      +log_out() bool
      +add_to_course(course: Course) bool
      +delete_from_course(course: Course) bool
      +register_payment(student: Student, payment_info: student.payment_infos)
    }
```

```mermaid
classDiagram
    class SystemAdmin{
      -user_name : String
      -password : String
      +new_system_admin() SystemAdmin
      +login_to_system()
      +add_new_branch(new_branch: SchoolBranch)
      +add_classroom(new_classroom: Classroom)
      +add_new_course(new_course: Course)
    }
```



* Yukarıda detayı verilen sınıfların detayları tekrar yazılmamıştır.

```mermaid
classDiagram
    SchoolBranch *-- Classroom 
    Classroom *-- Course
    class SchoolBranch{
        -name : String
        -id : String
        -address : String
        -public_transport : String
        -private_transport : String
        -social_benefits : vector~String~ 
        -classroom_list : vector~ClassRoom~ 
        -classroom_count : int
        +show_classrooms() : vector~ClassRoom~
        +find_classroom(classroom: Clasroom) int
        +add_classroom(classroom: Classroom) bool
        +delete_classroom(classroom: Classroom) bool
    }

    class Classroom{
        -name : String
        -capacity : int
        -course_list : vector~Course~
        -course_count : int
        -available_days : vector~String~
        -available_hours : vector~String~
        -available_time : dictionary<~String~, vector~String~>
        +set_available_times()
        +get_available_times() : vector~String~
        +find_course(course: Course) int
        +find_time(course: Course, day: String, hour: String) int
        +show_courses() : vector~Course~
        +add_course(course: Course) bool
        +delete_course(course: Course) bool       
    }

    class Course{
        -name : String
        -capacity : int
        -student_count : int
        -level : String
        -course_classroom : Classroom
        -student_list : vector~Student~
        -student_count : int
        -teacher : Teacher
        -date : Date
        +set_course_name(new_course_name: String) void
        +get_name() String
        +find_student(student: Student) int
        +add_student(new_student: Student) void
        +delete_student(student: Student) void
        +show_students()  vector~Student~
        +get_student_list() vector~Student~
        +show_students() void
        +check_course_time( course: Course) bool
    }
```

```mermaid
classDiagram
    class InformationSystem{
      -total_users : int
      -total_branches : int
      -worker_list : vector~Worker~
      -student_list : vector~Student~
      -teacher_list : vector~Teacher~
      -branch_list : vector~SchoolBranch~
      +get_teacher_list() : vector~Teacher~
    }
```


## Kaynaklar
[Class Diagram](https://mermaid-js.github.io/mermaid/#/classDiagram)
