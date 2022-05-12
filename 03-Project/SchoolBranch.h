#pragma once

namespace LanguageSchool
{
    class ClassRoom
    {
        // TODO: Maybe move this
    };

    class SchoolBranch
    {
        std::string name;
        std::string address;
        // M2 metro, T34, 500T bus
        std::string publicTransport;
        // Use 15 Temmuz Bridge
        std::string privateTransport;
        // table tennis, langırt, ...
        std::vector<std::string> socialBenefits;
        std::vector<ClassRoom> allClasses;
        bool isActiveBranch;
    };
} // LanguageSchool
