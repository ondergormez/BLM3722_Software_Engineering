#pragma once

#include <vector>
#include <string>

#include "Worker.h"
#include "SchoolBranch.h"

namespace LanguageSchool
{
    class Teacher : public Worker
    {
    public:
        std::vector<std::string> languages;
        std::vector<SchoolBranch> classLocations;
        std::string availableDays;
        std::string availableHours;
    };
} // LanguageSchool
