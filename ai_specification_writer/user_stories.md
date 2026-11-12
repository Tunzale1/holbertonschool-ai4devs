# User Stories — CarpoolConnect

Each story follows the format:
**As a** [role], **I want** [goal], **so that** [benefit].

Priority tags: **MVP** (launch-blocking), **High**, **Medium**, **Low**.
Stories are grouped by epic and trace to features in `product_idea.md`.

---

## Epic 1 — Onboarding & Identity

### User Story 1
As an **employee**, I want to sign in with my corporate SSO account so that I am automatically verified as a member of my organization.

**Acceptance Criteria**:
- User is authenticated via the organization's SAML/OIDC identity provider.
- The user's organization and role (employee/admin) are derived automatically from SSO claims.
- A user outside the organization's tenant cannot access the platform.

**Priority**: MVP

### User Story 2
As an **employee**, I want to create a profile with my commute preferences (home area, work location, schedule) so that I get relevant ride matches.

**Acceptance Criteria**:
- User can set home area, work location, and recurring commute schedule.
- Only minimal personal data is stored; sensitive data (phone, address) is opt-in.
- Profile changes are saved and reflected in future match results.

**Priority**: MVP

---

## Epic 2 — Ride Matching & Scheduling

### User Story 3
As a **passenger**, I want to search for colleagues driving my route at my commute time so that I can find a reliable ride quickly.

**Acceptance Criteria**:
- User enters pickup area, destination, and desired departure time.
- System returns matching drivers from the same organization, ranked by route and schedule fit.
- Only drivers with available seats are shown.

**Priority**: MVP

### User Story 4
As a **driver**, I want to publish a recurring trip with available seats so that passengers on my route can request to join.

**Acceptance Criteria**:
- Driver can define route, departure time, recurrence (e.g., weekdays), and seat count.
- Published trip is visible to matching passengers within the same organization.
- Driver can edit or cancel the trip, notifying any confirmed passengers.

**Priority**: MVP

### User Story 5
As a **passenger**, I want to request a seat and have the driver accept or decline so that both parties confirm the ride before it happens.

**Acceptance Criteria**:
- Passenger sends a seat request; driver receives a notification.
- Driver can accept or decline; passenger is notified of the outcome.
- A confirmed ride updates seat availability in real time.

**Priority**: MVP

### User Story 6
As a **driver**, I want the system to suggest route-optimal pickups so that detours are minimal and I still arrive on time.

**Acceptance Criteria**:
- System computes suggested pickup points that minimize added travel time/distance.
- Suggested pickups respect an estimated on-time arrival at the destination.
- Driver can accept the suggested pickup or propose an alternative.

**Priority**: High

---

## Epic 3 — Communication & Safety

### User Story 7
As a **passenger**, I want to message my driver in-app without revealing my phone number so that I can coordinate pickup while protecting my privacy.

**Acceptance Criteria**:
- Messaging is available only for confirmed rides.
- No personal phone numbers are exposed; messages are retained for audit.
- Messages can be reported for safety review.

**Priority**: MVP

### User Story 8
As an **employee**, I want to rate my ride and report safety concerns so that the community stays trustworthy and unsafe behavior is addressed.

**Acceptance Criteria**:
- User can submit a rating and optional review after a completed ride.
- User can file a safety report; it is routed to the corporate admin.
- Reported users can be flagged and reviewed per policy.

**Priority**: High

### User Story 9
As a **corporate admin**, I want to view and manage safety reports so that I can fulfill duty-of-care obligations.

**Acceptance Criteria**:
- Admin sees a queue of open safety reports for their organization.
- Admin can mark a report resolved with notes; action is auditable.
- Reports are retained per the organization's data-retention policy.

**Priority**: High

---

## Epic 4 — Cost Sharing & Payments

### User Story 10
As a **driver**, I want the cost of each ride split transparently among passengers so that I fairly recover fuel and parking costs.

**Acceptance Criteria**:
- Per-seat cost is computed from a configurable formula (distance × rate).
- Each passenger sees the cost before confirming the ride.
- Settlement happens via the organization's configured payment method (wallet/reimbursement).

**Priority**: High

### User Story 11
As a **corporate admin**, I want to configure cost-sharing rules so that reimbursements comply with company policy and local tax rules.

**Acceptance Criteria**:
- Admin can set per-seat caps, eligible rates, and payment method.
- Rules are enforced at ride confirmation and settlement.
- Changes to rules apply to future rides and are logged.

**Priority**: Medium

---

## Epic 5 — Admin & ESG Reporting

### User Story 12
As a **corporate admin**, I want a dashboard of commute metrics so that I can demonstrate parking relief and progress toward ESG targets.

**Acceptance Criteria**:
- Dashboard shows participation rate, SOV reduction, and estimated CO₂ saved.
- Metrics are filterable by date range, team, and location.
- Data updates at least daily.

**Priority**: MVP

### User Story 13
As a **corporate admin**, I want to export compliance and ESG reports so that I can include them in sustainability and audit reporting.

**Acceptance Criteria**:
- Admin can export reports (CSV/PDF) for a selected period.
- Exported reports include methodology notes for CO₂ calculations.
- Exports respect the organization's data-residency policy.

**Priority**: Medium

---

## Epic 6 — Platform Administration

### User Story 14
As a **platform/IT administrator**, I want to manage organization tenants and roles so that access is governed and auditable.

**Acceptance Criteria**:
- Admin can create/deactivate tenants and assign roles (employee, admin).
- All role and tenant changes are written to an audit log.
- SSO configuration can be tested before enabling for users.

**Priority**: Medium