# High-Value Brainstorming Methods for Software Discovery

> **Expert's Note:** In the software industry, "Brainstorming" is often misunderstood as just sitting in a room and shouting ideas. High-value outcomes come from **Structured Brainstorming**. These are methods designed to extract specific types of logic (Technical, User, or Strategic) and convert them into the "Product Constitution."

---

## 1. Event Storming (The Logic-Touch Favorite)
This is the gold standard for mapping out complex systems and business logic.

*   **WHAT:** A workshop-based method to map out a complex business domain using "Domain Events" (things that happened) on a timeline.
*   **WHY:** It rapidly surface's technical complexity, hidden edge cases, and "bounded contexts" that a PRD might miss. It is the bridge between a PM's vision and an Architect's database schema.
*   **HOW:** Participants use orange sticky notes to represent "Events" (e.g., *OrderPlaced*, *PaymentFailed*). You lay them out chronologically and then identify the "Commands" that triggered them and the "Policies" that govern them.
*   **WHEN:** During the transition from **Product Strategy** to **High-Detail PRD**. Use it when the logic is "dense."

## 2. Design Sprints (The Strategic Accelerator)
Developed at Google Ventures to solve big problems and test ideas in just 5 days.

*   **WHAT:** A 5-phase process: Map, Sketch, Decide, Prototype, and Test.
*   **WHY:** To bypass the months of debate and build a high-fidelity prototype that is validated by real users before a single line of code is written.
*   **HOW:** A cross-functional group (PM, Designer, Architect) works through intense exercises to narrow down a massive problem into a single, testable hypothesis.
*   **WHEN:** At the **very beginning of a new product or major feature** (The "Vision to Strategy" phase).

## 3. Impact Mapping (The Outcome Anchor)
A technique that prevents "Feature Creep" by linking every requirement to a business goal.

*   **WHAT:** A visual map that starts with a **Goal**, then identifies **Actors**, **Impacts**, and finally **Deliverables**.
*   **WHY:** It ensures that the "Logic-Touch" and "No-Code" groups don't build features that have zero impact on the business objective.
*   **HOW:** You ask: *Why* are we doing this? (Goal) -> *Who* can help or hinder us? (Actors) -> *How* should their behavior change? (Impact) -> *What* can we do to support that change? (Deliverables).
*   **WHEN:** During **Strategic Planning** to define the scope of a PRD.

## 4. Working Backwards (The Amazon Press Release)
Forces the team to think from the user's perspective on day one.

*   **WHAT:** You write the **Press Release (PR)** and the **Frequently Asked Questions (FAQ)** for the product *before* you write the PRD.
*   **WHY:** If the PR doesn't sound exciting, the product isn't worth building. It crystalizes the "Value Proposition" in human language.
*   **HOW:** The PM writes a mock press release announcing the launch. It must describe the problem, the solution, and a quote from a satisfied user.
*   **WHEN:** At the **Vision phase**. It sets the "Constitutional" tone for everything that follows.

## 5. Pre-Mortems (The Risk Shield)
A psychological technique to identify failures before they happen.

*   **WHAT:** The team imagines the project has **completely failed** one year from now and brainstorms all the reasons why.
*   **WHY:** Humans are naturally optimistic. A Pre-Mortem removes the bias and allows Architects and PMs to identify "Black Swan" risks (technical, market, or operational).
*   **HOW:** "Imagine we launched and the app crashed on day one for 100% of users. Why?" -> "The Cloud Architect forgot to set up auto-scaling." -> Result: Add Auto-scaling to the PRD.
*   **WHEN:** Just before the **PRD is finalized** (Ratification phase).

---

## 🎯 Summary Matrix: Which Method to Use?

| Goal | Best Method | Primary Participants |
| :--- | :--- | :--- |
| **Understand Complex Logic** | Event Storming | Architects, PMs, Devs |
| **Validate a New Concept** | Design Sprint | PM, UX, Prototype Dev |
| **Align Features to Goals** | Impact Mapping | Stakeholders, PM, EM |
| **Define User Value** | Working Backwards | CEO, PM, UX |
| **De-risk the Plan** | Pre-Mortem | All (Cross-functional) |

**Veteran's Advice:** Don't use all of them at once. Pick the one that solves your current "Information Gap." If you don't know *what* to build, use a **Design Sprint**. If you know what to build but not *how* it works, use **Event Storming**.
