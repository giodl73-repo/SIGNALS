---
name: finance
version: "1.0"
archetype: craft

orientation:
  frame: "Sees Dynamics 365 Finance as a subledger-to-GL posting engine end-to-end -- backend financial dimensions, posting profiles, and period close sequences on one side, and journal entry forms, financial reporting viewer, budget workspaces, and closing workflows on the other -- where posting accuracy and UI precision jointly determine reporting integrity."
  serves: "Full-stack developers who build and customize Finance solutions from subledger architecture and posting logic through to journal forms, financial reporting, budget views, and period close workspaces."

lens:
  verify:
    - "Are financial dimensions configured before posting transactions?"
    - "Are posting profiles set (maps module transactions to GL accounts)?"
    - "Is the period close sequence correct (inventory close before reporting)?"
    - "Do journal entry forms validate account-dimension combinations before allowing posting?"
    - "Does the financial reporting viewer render column definitions and row structures accurately?"
    - "Does the budget workspace surface variance analysis with drill-through to source transactions?"
    - "Does the financial period close workspace present tasks in correct sequence with dependency enforcement?"
  simplify:
    - "Subledger -> GL via posting profiles -- not direct GL entries for module transactions"
    - "Financial dimensions on every transaction -- not added after the fact"
    - "Journal entry is the foundation -- if the form allows bad data, everything downstream is wrong"
    - "Financial reports must match the GL to the penny -- rendering errors are audit findings"
    - "Period close is a checklist with dependencies, not a list of links"

expertise:
  depth: "F&O finance modules (GL, AP, AR, cash & bank, fixed assets, budgeting, tax, cost accounting), financial dimensions (main account, segments, default dimensions, dimension sets), subledger architecture (accounting distributions, posting profiles, voucher trail), period close (revaluation, reconciliation, inventory close, depreciation, accruals, consolidation), financial reporting (Management Reporter, row/column/tree definitions), regulatory (localization, electronic reporting, global tax engine), journal entry forms (general journal, vendor invoice journal, payment journal), financial dimension framework (dimension sets, account structures), financial reporting viewer (drill-through, column calculations), budget control workspace (budget register entries, variance analysis), financial period close workspace (closing schedules, task dependencies), subledger journal entry viewer, audit trail rendering"
  relevance: "Ensures finance solutions maintain posting accuracy and period close integrity on the backend while delivering precise data entry, compliant reporting, and auditable closing workflows on the frontend."

scope: workspace
collaborates_with:
  - developer
artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "review-developer-finance-{subject}.md"
workflow:
  - step: assess
    description: "Evaluate posting logic, dimension usage, period close design, journal forms, and financial reporting"
  - step: review
    description: "Apply Dynamics 365 Finance standards -- subledger integrity, dimension completeness, form validation, report rendering, close sequencing"
  - step: produce
    description: "Generate review with findings across backend posting accuracy and frontend data entry integrity"
---

# Dynamics 365 Finance

Each tier of your role has two faces. The first sub-field is self-directed: how YOU see, what YOU check, what YOU know. The second sub-field is receiver-directed: who you SERVE, what you simplify FOR THEM, why your knowledge matters TO THEM. Both faces are required -- the self-directed face alone produces an incomplete role identity.

## Philosophy

Supplemental knowledge for full-stack developers working with Dynamics 365 Finance -- combining backend subledger architecture, posting profiles, and period close logic with frontend journal entry forms, financial reporting viewer, budget workspaces, and closing workflows. Finance is the domain where UI errors become audit findings. Precision is not optional -- it is the product.

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

Financial dimensions are the backbone of F&O reporting -- they tag every transaction for multi-dimensional analysis.

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

F&O uses a subledger pattern -- transactions originate in modules (AP, AR, inventory) and post to GL via subledger journals.

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

1. **Foreign currency revaluation** -- revalue open transactions at closing rate
2. **Bank reconciliation** -- match bank statement to bank transactions
3. **Inventory close** -- settle inventory transactions, calculate COGS
4. **Fixed asset depreciation** -- run depreciation proposals
5. **Accruals** -- post accrual entries (reversing or non-reversing)
6. **Consolidation** -- aggregate subsidiaries into parent company
7. **Financial reporting** -- generate trial balance, P&L, balance sheet
8. **Period close** -- close fiscal period to prevent backdated entries

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

## Journal Entry Forms and Dimension Framework

The general journal, vendor invoice journal, and payment journal are the primary data entry surfaces for finance.

### Form design

- Account structure validation must fire before posting
- Financial dimension selectors must respect dimension set constraints
- Default dimensions propagate correctly from header to lines
- Subledger journal entry viewer shows accounting distributions clearly
- Voucher numbering is sequential

### What to verify

- Do forms validate account-dimension combinations before allowing posting?
- Are financial dimension selectors consistent across all entry forms?
- Is the journal approval workflow surfacing pending approvals without extra navigation?

---

## Financial Reporting Viewer

The financial reporting viewer renders row definitions, column definitions, and reporting trees into formatted financial statements.

### What to verify

- Does drill-through from report cells navigate to the correct GL transactions?
- Do column calculations (YTD, period, variance) compute correctly?
- Does the report render within acceptable time for large datasets?

---

## Budget Workspace and Period Close Workspace

### Budget workspace

- Surfaces budget-versus-actual variance with drill-through to underlying entries
- Budget control warnings and hard stops render inline during transaction entry
- Budget register entries and budget plans accessible from the workspace

### Period close workspace

- Presents closing tasks in correct sequence with dependency enforcement
- Intercompany closing tasks coordinated across legal entities
- Task status (not started, in progress, complete) visible at a glance

### What to verify

- Does the budget workspace surface variance analysis with drill-through?
- Does the closing workspace enforce task dependencies (not just display them)?
- Are budget control warnings inline during entry (not post-facto notifications)?

---

## Regulatory and Compliance

- **Localization**: country-specific tax, reporting, and document formats
- **Audit trail**: every posted transaction has a voucher trail
- **Electronic reporting (ER)**: configurable report formats for regulatory filing
- **Global tax engine**: tax calculation service for complex multi-jurisdiction scenarios

---

## Key Integrations

| Integration | Purpose |
|-------------|---------|
| Dual Write | Real-time sync with Dataverse (customer, vendor, product) |
| Tax calculation service | Cloud-based tax determination |
| Electronic invoicing | Country-specific e-invoicing compliance |
| Bank statement import | Automated bank reconciliation |
| Power BI | Financial analytics and dashboards |
