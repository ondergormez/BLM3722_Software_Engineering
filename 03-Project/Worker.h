#pragma once

#include <string>

#include "Person.h"

namespace LanguageSchool
{
    class Worker : public Person
    {
        std::string workStartDate;
        std::string workEndDate;
        bool isActiveWorker;
        int salary;
    };
} // LanguageSchool
