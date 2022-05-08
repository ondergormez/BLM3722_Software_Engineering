#pragma once

#include <string>
#include <vector>

#include "Person.h"

namespace LanguageSchool
{
    // student.updateName("Batuhan")
    // REQUIRE(student.getName() == "Batuhan")
    class Student : public Person
    {

    public:
        void updateName(std::string newName);
        std::string getName();

    private:
        std::vector<std::string> courses;
        std::vector<std::string> courseLevel;
        std::string paymentInfos;
    }

} // LanguageSchool
