# Product Idea — CarpoolConnect

## Vision
Make the daily commute cheaper, greener, and less stressful by enabling employees
of the same organization to share rides through a trusted, employer-sponsored
platform. CarpoolConnect turns fragmented, informal carpooling into a managed,
measurable, and compliant corporate benefit.

> "Every empty seat on the morning commute is a missed opportunity — for the
> commuter, the employer, and the planet."

## Primary Users & Their Needs

### 1. Employees — Drivers
- **Needs:** Fill empty seats, offset fuel/parking costs, reduce solo-driving
  fatigue, feel safe sharing with verified colleagues.
- **Pain points:** No trusted pool of riders; awkward cost-splitting; no
  visibility into who is traveling when.
- **Success:** Seats filled on a predictable schedule with minimal coordination.

### 2. Employees — Passengers
- **Needs:** Affordable, reliable, safe rides to/from the workplace; flexible
  scheduling; confidence in the driver's identity.
- **Pain points:** Unreliable public transport, high ride-hail costs, no
  trusted carpool network inside the company.
- **Success:** A confirmed, on-time ride at a fraction of ride-hail cost.

### 3. Corporate Admin / HR / Facilities (Buyer persona)
- **Needs:** Reduce parking demand, meet ESG/sustainability targets, offer a
  tangible commute benefit, ensure policy compliance and duty-of-care.
- **Pain points:** No data on commute patterns; parking congestion; fragmented
  benefit programs; compliance/liability concerns.
- **Success:** Measurable reduction in single-occupancy vehicles (SOV) and CO₂,
  backed by dashboards and reports.

### 4. Platform / IT Administrator (secondary)
- **Needs:** SSO/identity integration, role management, auditability, data
  residency and privacy compliance.
- **Success:** Low-friction onboarding via existing corporate identity provider.

## Key Features

### Core (MVP)
- **Corporate onboarding & SSO** — Tenant per organization, integrated with
  corporate identity (SAML/OIDC), role-based access (employee, admin).
- **Verified ride matching** — Match drivers and passengers within the same
  organization based on route, schedule, and preferences; show match quality
  and confidence.
- **Ride scheduling & seat management** — Recurring and one-off trips, seat
  capacity, accept/decline workflow, ride status lifecycle.
- **In-app messaging (privacy-preserving)** — Coordinate pickup without
  exposing personal phone numbers; moderated, auditable.
- **Cost-sharing & payment** — Transparent per-seat cost calculation and
  settlement (corporate wallet, reimbursement, or integrated payments).
- **Ratings, reviews & trust signals** — Post-ride feedback, verified profiles,
  safety reporting.
- **Admin dashboard & ESG reporting** — Parking utilization, SOV reduction,
  CO₂ savings, participation rates, exportable compliance reports.

### Differentiators
- **Employer-sponsored trust boundary** — Matches are restricted to verified
  colleagues, solving the core safety/adoption problem of public carpool apps.
- **ESG-first analytics** — Built-in sustainability metrics and reporting
  aligned to corporate ESG frameworks, not bolted on.
- **Policy & duty-of-care engine** — Configurable corporate policies (eligibility,
  cost caps, safety rules) enforced by the platform.
- **Commute-aware scheduling** — Optimized for predictable daily commute
  patterns (shift workers, hybrid schedules), not one-off long-distance trips.
- **Privacy by design** — Minimal personal data exposure, auditable messaging,
  GDPR-ready data handling.

## Out of Scope (Initial Release)
- Consumer (non-corporate) marketplace features.
- Long-distance/intercity trip planning.
- Autonomous vehicle or fleet-ownership management.
- Native mobile apps may be phased after a responsive web MVP (decision pending
  in technical spec).

## Assumptions & Constraints
- Organizations provide identity integration (SSO) and approve the benefit.
- Local carpooling/payment regulations must be configurable per region.
- Safety and privacy compliance are non-negotiable, launch-blocking concerns.

## Open Questions (to resolve in subsequent specs)
- Payment model: corporate-subsidized vs. peer-to-peer settlement?
- Mobile-first native apps vs. PWA for MVP?
- Which ESG reporting standard(s) to support first?
- Geographic launch scope and regulatory constraints?