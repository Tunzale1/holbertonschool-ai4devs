# Codebase Overview – Legacy COBOL Accounting System

## 1. Project Age

- **Project:** Legacy COBOL Accounting System
- **Repository:** continuous-copilot/modernize-legacy-cobol-app
- **First recorded Git commit:** February 22, 2025
- **Latest recorded Git commit:** February 22, 2025
- **Approximate age:** 1 year and 9 months as of November 2026.

The repository contains a legacy-style COBOL accounting application designed to demonstrate the modernization of an existing COBOL system into a Node.js application.

## 2. Codebase Size (LOC)

The application contains approximately **99 lines of COBOL source code** across three source files.

| File | Lines of Code | Responsibility |
|---|---:|---|
| main.cob | 36 | Main menu and user interaction |
| operations.cob | 40 | Account balance, credit, and debit operations |
| data.cob | 23 | Balance storage and read/write operations |
| **Total** | **99** | **COBOL source code** |

### Programming Language
- COBOL

## 3. Main Dependencies

### Runtime and Compiler
- **GnuCOBOL:** Open-source COBOL compiler required to compile and execute the application.

### Development Tools
- Visual Studio Code or another supported IDE.
- COBOL editor extension.
- GitHub Copilot and GitHub Copilot Chat for AI-assisted development.

### External Libraries
- No external COBOL application libraries are declared in the inspected source files.
- The application primarily uses standard COBOL language features.

## 4. Application Architecture

The application is divided into three COBOL programs:

- **main.cob:** Displays the account management menu and handles user selections.
- **operations.cob:** Implements balance viewing, crediting, and debiting operations.
- **data.cob:** Manages reading and writing the account balance.

The application supports the following operations:

1. View the current account balance.
2. Credit an account.
3. Debit an account.
4. Exit the application.

The initial account balance is 1000.00.

## 5. Known Issues and Technical Pain Points

The following issues were identified through inspection of the source code and project documentation.

### 5.1 Lack of Persistent Data Storage
The account balance is stored in a COBOL WORKING-STORAGE variable. Changes are not saved to an external database or file, meaning the balance resets when the application restarts.

### 5.2 Limited Input Validation
The application accepts user input without comprehensive validation. Invalid amounts, negative values, and unexpected input may cause incorrect behavior or runtime errors.

### 5.3 Limited Error Handling
The application does not provide comprehensive handling for invalid operations, unexpected input, or failures during program execution.

### 5.4 No Automated Tests
The project README explicitly identifies the absence of tests for the existing COBOL application. This makes regression testing and verification of business logic more difficult.

### 5.5 Limited Scalability
The application manages a single account balance and does not implement multiple accounts, customer records, or transaction history.

### 5.6 Tight Module Interfaces
The three programs communicate through COBOL CALL statements and fixed-length data fields. Changes to these interfaces may require coordinated modifications across multiple programs.

## 6. Modernization Opportunities

The following improvements could address the identified limitations:

- Introduce persistent storage using a database.
- Implement comprehensive input validation and error handling.
- Create automated unit and integration tests.
- Separate business logic from user interface functionality.
- Introduce support for multiple accounts and transaction history.
- Migrate the application from COBOL to Node.js, as proposed in the repository documentation.
- Document program interfaces and business rules.
- Use AI-assisted code analysis to explain existing functionality and support safe refactoring.

## 7. Conclusion

The Legacy COBOL Accounting System is a small, modular accounting application consisting of three COBOL programs and approximately 99 lines of source code.

Although the application demonstrates basic separation of responsibilities, it has limitations involving data persistence, input validation, error handling, automated testing, and scalability.

Modernization using Node.js, improved testing practices, and persistent data storage would help address these limitations while preserving the existing accounting functionality.

**Repository:** continuous-copilot/modernize-legacy-cobol-app  
**Original language:** COBOL  
**Compiler:** GnuCOBOL  
**Total source LOC:** 99  
**Documentation file:** codebase_overview.md