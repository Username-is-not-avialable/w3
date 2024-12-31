// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DiplomaRegistry {
    // Структура для хранения информации о дипломе
    struct Diploma {
        string ownerName;  // Имя владельца диплома
        string university; // Учебное заведение
        string degree;     // Специальность
        string date;       // Дата выдачи
        bool exists;       // Проверка существования диплома
    }

    // Хранение дипломов по их ID (например, хэш или номер)
    mapping(string => Diploma) private diplomas;

    // Адреса авторизованных учебных заведений
    mapping(address => bool) public authorizedUniversities;

    // Владелец контракта
    address public owner;

    // Событие для добавления диплома
    event DiplomaAdded(string diplomaId, string ownerName, string university);

    constructor() {
        owner = msg.sender; // Владелец контракта — создатель
    }

    // Функция для добавления учебного заведения
    function authorizeUniversity(address university) public {
        require(msg.sender == owner, "Only owner can authorize universities");
        authorizedUniversities[university] = true;
    }

    // Функция для добавления диплома
    function addDiploma(
        string memory diplomaId,
        string memory ownerName,
        string memory university,
        string memory degree,
        string memory date
    ) public {
        require(authorizedUniversities[msg.sender], "Not authorized");

        require(!diplomas[diplomaId].exists, "Diploma already exists");

        diplomas[diplomaId] = Diploma(ownerName, university, degree, date, true);

        emit DiplomaAdded(diplomaId, ownerName, university);
    }

    // Функция для получения информации о дипломе
    function getDiploma(string memory diplomaId)
        public
        view
        returns (string memory, string memory, string memory, string memory)
    {
        require(diplomas[diplomaId].exists, "Diploma not found");
        Diploma memory diploma = diplomas[diplomaId];
        return (diploma.ownerName, diploma.university, diploma.degree, diploma.date);
    }
}
