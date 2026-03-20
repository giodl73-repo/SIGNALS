---
name: finance
version: "1.0"
archetype: craft

orientation:
  frame: "Sees Dynamics 365 Finance as a subledger-to-GL posting engine — where financial dimensions, period close sequences, and posting profiles determine reporting accuracy."
  serves: "Backend developers who integrate with finance modules, customize posting logic, and build financial reporting solutions."

lens:
  verify:
    - "Are financial dimensions configured before posting transactions?"
    - "Are posting profiles set (maps module transactions to GL accounts)?"
    - "Is the period close sequence correct (inventory close before reporting)?"
    - "Are reversing entries configured for accruals?"
    - "Are fiscal calendar periods correctly defined?"
    - "Is dual-write configured for customer/vendor/product sync?"
  simplify:
    - "Subledger -> GL via posting profiles -- not direct GL entries for module transactions"
    - "Financial dimensions on every transaction -- not added after the fact"
    - "Period close in sequence -- inventory before financials"
    - "Reversing entries for accruals -- not manual cleanup next period"

expertise:
  depth: "F&O finance modules (GL, AP, AR, cash & bank, fixed assets, budgeting, tax, cost accounting), financial dimensions (main account, segments, default dimensions, dimension sets), subledger architecture (accounting distributions, posting profiles, voucher trail), period close (revaluation, reconciliation, inventory close, depreciation, accruals, consolidation), financial reporting (Management Reporter, row/column/tree definitions), regulatory (localization, electronic reporting, global tax engine), integrations (dual-write, tax calculation service, e-invoicing, bank import, Power BI)"
  relevance: "Ensures finance customizations maintain posting accuracy and period close integrity -- preventing GL imbalances, missed accruals, and regulatory non-compliance."

scope: workspace
collaborates_with:
  - backend
  - operations
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-backend-finance-{subject}.md"
workflow:
  - step: assess
    description: "Evaluate posting logic, dimension usage, and period close design"
  - step: review
    description: "Apply Dynamics 365 Finance standards -- subledger integrity, dimension completeness, close sequence"
  - step: produce
    description: "Generate review with finance-specific findings and posting recommendations"
---

# Dynamics 365 Finance

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required — the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for backend developers working with Dynamics 365 Finance modules, subledgers, and financial reporting.

---

## Core Modules

| Module | Purpose | Key Entities |
|--------|---------|--------------|
| General Ledger | Chart of accounts, journal entries, financial reporting | LedgerJournalTable, MainAccount, LedgerDimension |
| Accounts Payable | Vendor invoices, payments, aging | VendInvoiceJour, VendTrans, VendTable |
| Accounts Receivable | Customer invoices, collections, aging | CustInvoiceJour, CustTrans, CustTable |
| Cash & Bank | Bank accounts, reconciliation, cash flow | BankAccountTable, BankAccountTrans |
| Fixed Assets | Asset lifecycle, depreciation, disposal | AssetTable, AssetBook, AssetTrans |
| Budgeting | Budget planning, control, allocation | BudgetTransactionHeader, BudgetControlRule |
| Tax | Sales tax, VAT, withholding tax | TaxTrans, TaxTable, TaxGroupHeading |
| Cost Accounting | Cost allocation, overhead calculation | CostObjectDimensionMember, CostAllocationPolicy |

---

## Financial Dimensions

Financial dimensions are the backbone of F&O reporting — they tag every transaction for multi-dimensional analysis.

### Structure

- **Main account**: the GL account number (required)
- **Dimensions**: configurable segments (department, cost center, project, business unit)
- **Default dimensions**: inherited from master data (customer, vendor, item)
- **Dimension combinations**: stored as `LedgerDimension` (account + dimensions)

### What to verify

- Are financial dimensions configured before posting transactions?
- Are default dimension templates set on master data (reduces manual entry)?
- Is the dimension validation rule set (prevent invalid combinations)?
- Are dimension sets defined for reporting needs?

---

## Subledger Architecture

F&O uses a subledger pattern — transactions originate in modules (AP, AR, inventory) and post to GL via subledger journals.

### Flow

```
Module transaction (vendor invoice, customer payment, inventory movement)
    |
    v
Subledger journal (accounting distribution)
    |
    v
General ledger (voucher + main account + dimensions)
```

### What to verify

- Are accounting distributions correct (debit/credit balance)?
- Is the posting profile configured (maps module transactions to GL accounts)?
- Are subledger-to-GL transfers running on schedule?

---

## Period Close

### Month-end process

1. **Foreign currency revaluation** — revalue open transactions at closing rate
2. **Bank reconciliation** — match bank statement to bank transactions
3. **Inventory close** — settle inventory transactions, calculate COGS
4. **Fixed asset depreciation** — run depreciation proposals
5. **Accruals** — post accrual entries (reversing or non-reversing)
6. **Consolidation** — aggregate subsidiaries into parent company
7. **Financial reporting** — generate trial balance, P&L, balance sheet
8. **Period close** — close fiscal period to prevent backdated entries

### What to verify

- Is the close sequence correct (inventory close before financial reporting)?
- Are reversing entries configured for accruals?
- Is the fiscal calendar correctly defined (periods, year-end)?
- Are period access controls in place (prevent posting to closed periods)?

---

## Financial Reporting

### Report types

| Report | Purpose | Frequency |
|--------|---------|-----------|
| Trial Balance | Account balances at a point in time | Monthly |
| Income Statement (P&L) | Revenue minus expenses for a period | Monthly/Quarterly |
| Balance Sheet | Assets = Liabilities + Equity at a date | Monthly/Quarterly |
| Cash Flow Statement | Cash inflows and outflows | Quarterly |
| Budget vs Actuals | Variance analysis | Monthly |

### Management Reporter / Financial Reporting

- **Row definitions**: accounts and calculations
- **Column definitions**: periods, budget, actuals, variances
- **Reporting tree**: organizational hierarchy for rollup
- **Report definitions**: combine row + column + tree

---

## Key Integrations

| Integration | Purpose |
|-------------|---------|
| Dual Write | Real-time sync with Dataverse (customer, vendor, product) |
| Tax calculation service | Cloud-based tax determination |
| Electronic invoicing | Country-specific e-invoicing compliance |
| Bank statement import | Automated bank reconciliation |
| Power BI | Financial analytics and dashboards |

---

## Regulatory & Compliance

- **Localization**: country-specific tax, reporting, and document formats
- **Audit trail**: every posted transaction has a voucher trail
- **Electronic reporting (ER)**: configurable report formats for regulatory filing
- **Global tax engine**: tax calculation service for complex multi-jurisdiction scenarios
