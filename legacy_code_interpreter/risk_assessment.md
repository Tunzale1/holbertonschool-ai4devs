# Risk Assessment – Legacy COBOL Accounting System

## 1. Introduction

This document identifies and evaluates potential risks in the Legacy COBOL Accounting System.

The assessment is based on the inspection of the following source files:

- `main.cob`
- `operations.cob`
- `data.cob`

The objective is to identify technical and operational risks, assign severity levels, and recommend improvements to support safe modernization.

## 2. Risk Assessment Table

| Risk | Severity | Source / Evidence | Notes and Potential Impact | Recommended Mitigation |
|---|---|---|---|---|
| Lack of persistent data storage | High | `data.cob` – `STORAGE-BALANCE` | The account balance is stored in memory. Changes are lost when the application terminates. | Introduce persistent database or file storage. |
| Insufficient input validation | High | `main.cob`, `operations.cob` | User input is accepted without comprehensive validation. Invalid or unexpected amounts may cause incorrect behavior. | Validate input types, ranges, and transaction amounts before processing. |
| Negative transaction amounts | High | `operations.cob` – CREDIT and DEBIT operations | The application does not explicitly reject negative amounts. This could result in unintended balance changes. | Reject negative and zero transaction amounts according to business rules. |
| Lack of automated tests | High | Project README and `TESTPLAN.md` | The README identifies that the original COBOL application has no automated tests. Changes may introduce undetected regressions. | Implement unit and integration tests for all business operations. |
| Limited error handling | Medium | `main.cob`, `operations.cob`, `data.cob` | Unexpected input and invalid storage commands are not comprehensively handled. | Introduce structured error handling and meaningful error messages. |
| Single-account limitation | Medium | `data.cob` – `STORAGE-BALANCE` | The application maintains only one account balance and does not support multiple customers or accounts. | Introduce account identifiers and a scalable data model. |
| No transaction history or audit trail | Medium | `operations.cob`, `data.cob` | Credit and debit operations update the balance without recording transaction details. This limits traceability and auditing. | Maintain transaction records with timestamps, amounts, and transaction types. |
| Tight coupling through program interfaces | Medium | `main.cob`, `operations.cob`, `data.cob` | Programs communicate through fixed-length parameters and COBOL CALL statements. Interface changes may affect multiple modules. | Define clear interfaces and separate business logic from application control. |

## 3. Risk Severity Classification

The following classification is used:

- **High:** Risks that may directly affect financial correctness, data reliability, or the ability to verify application behavior.
- **Medium:** Risks that may affect maintainability, scalability, traceability, or operational reliability.
- **Low:** Issues with limited impact that do not significantly affect core application functionality.

## 4. Risk Prioritization

### High-Priority Risks

1. **Lack of persistent data storage:** Account balances are not preserved after application termination.
2. **Insufficient input validation:** Invalid input can affect account operations.
3. **Negative transaction amounts:** Unvalidated amounts can produce unintended financial results.
4. **Lack of automated tests:** There is no automated safety net to verify existing business logic.

These risks should be addressed before deploying a modernized application.

### Medium-Priority Risks

1. **Limited error handling:** Unexpected situations may not be handled gracefully.
2. **Single-account limitation:** The application cannot support a larger multi-account environment.
3. **No transaction history:** Financial operations cannot be easily audited.
4. **Tight coupling:** Changes to program interfaces may require coordinated modifications.

These risks should be addressed as part of the modernization and architectural improvement process.

## 5. Recommended Mitigation Strategy

The following actions are recommended:

1. Introduce database-backed persistent storage.
2. Implement strict validation for menu selections and transaction amounts.
3. Prevent zero and negative transactions.
4. Create automated tests for balance viewing, crediting, debiting, and insufficient funds.
5. Improve error handling and input-related error messages.
6. Design a data model that supports multiple accounts.
7. Implement transaction logging and audit functionality.
8. Refactor program interfaces to improve modularity and maintainability.

## 6. Conclusion

The assessment identifies eight risks in the Legacy COBOL Accounting System.

The highest-priority concerns involve data persistence, input validation, transaction correctness, and the absence of automated tests.

Addressing these risks during modernization will help create a more reliable, maintainable, and scalable accounting application.

The risk assessment provides a foundation for prioritizing improvements before migrating the existing COBOL functionality to Node.js.