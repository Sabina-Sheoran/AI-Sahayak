# Design System Document

## 1. Overview & Creative North Star: "The Digital Hearth"

This design system is built upon the concept of **"The Digital Hearth."** In a rural context, the hearth is a point of warmth, reliability, and communal gathering. We translate this into a digital experience that rejects the cluttered, "noisy" interface of traditional utility apps. Instead, we embrace **Soft Functionalism**: a high-contrast, ultra-legible editorial style that feels premium yet deeply intuitive.

To support low-literacy users, we move beyond the "grid of icons." We utilize **intentional asymmetry** and **tonal layering** to guide the eye. Large, generous hit areas and a "Type-First" hierarchy ensure that whether a user is reading English or Hindi, the information is authoritative and easy to digest. This is not just a tool; it is a trustworthy assistant.

---

## 2. Colors & Surface Philosophy

The color palette is anchored by a vibrant, earthy orange, balanced by a sophisticated range of tonal greys and whites.

### The "No-Line" Rule
To achieve a high-end, modern feel, **1px solid borders are strictly prohibited** for sectioning. We define boundaries through background color shifts. 
- Use `surface-container-low` (#f3f3f3) sections sitting on a `surface` (#f9f9f9) background.
- Contrast is achieved through the proximity of tonal shifts, not "ink" lines.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of fine paper.
- **Base Layer:** `surface` (#f9f9f9)
- **Content Blocks:** `surface-container-low` (#f3f3f3)
- **High-Priority Floating Cards:** `surface-container-lowest` (#ffffff)
- **Interactive Deep Layers:** `surface-container-high` (#e8e8e8)

### The Glass & Gradient Rule
For main Call-to-Actions (CTAs) and Hero sections, avoid flat fills. Use a subtle linear gradient from `primary` (#a03b00) to `primary-container` (#c94c00) at a 135-degree angle. This adds "soul" and a tactile, sun-drenched quality to the warm orange.

---

## 3. Typography: The Editorial Voice

We utilize **Public Sans** for its high x-height and exceptional legibility in both Latin and Devanagari scripts.

*   **Display (lg/md/sm):** Use for "Momentum" screens—onboarding or success states. These should be bold and authoritative.
*   **Headline (lg/md/sm):** Used for section headers. In Hindi, ensure line-height is increased by 1.2x to prevent "Matra" (vowel markers) from clashing.
*   **Title (lg/md/sm):** These are your primary navigation and card labels. They must be high-contrast (`on-surface`).
*   **Body (lg/md):** Reserved for instructional text. Never go below `body-md` (0.875rem) for critical livelihood information.
*   **Labels:** Use sparingly for metadata.

**Hierarchy Strategy:** To move away from a "template" look, use `display-md` next to `body-lg` with a wide `spacing-6` (2rem) gap to create an editorial, airy feel.

---

## 4. Elevation & Depth: Tonal Layering

We reject the "drop shadow" of 2010. Depth in this system is organic.

*   **The Layering Principle:** A card should be defined by being `surface-container-lowest` (#ffffff) placed on a `surface-container` (#eeeeee) background. The 12-step color difference provides the "lift."
*   **Ambient Shadows:** If a floating action button (FAB) or critical modal requires a shadow, use a blur of `24px` with 6% opacity using the `on-surface` color. It should feel like a soft glow, not a dark stain.
*   **The Ghost Border:** If a boundary is required for accessibility in high-sunlight environments, use the `outline-variant` (#e1bfb3) at **15% opacity**. This creates a "suggestion" of a container without breaking the minimal aesthetic.
*   **Glassmorphism:** For top navigation bars, use `surface` at 80% opacity with a `20px` backdrop blur. This allows the warm orange of the content to bleed through as the user scrolls, maintaining a sense of place.

---

## 5. Components

### Buttons (The "Tappable Target")
*   **Primary:** Gradient fill (`primary` to `primary-container`), `roundness-lg` (1rem). Padding should be `spacing-4` (1.4rem) on the Y-axis to ensure a massive hit area for rural users.
*   **Secondary:** `surface-container-highest` (#e2e2e2) with `on-surface` text. No border.
*   **Tertiary:** Transparent background, `primary` text, bold weight.

### Cards & Lists
*   **Rule:** **No dividers.**
*   Use `spacing-3` (1rem) of vertical white space to separate list items.
*   Wrap related content in a `surface-container-low` card with `roundness-md`.

### Input Fields
*   **Style:** Filled backgrounds (`surface-container-high`) with a bottom-only "heavy" indicator in `primary` (2px) when focused. 
*   **Labels:** Always persistent. Never use placeholder text as a label, as it disappears and confuses low-literacy users.

### Voice-First Interface (Context Specific)
*   **The Pulse:** A large, circular `primary` button featuring a `white` microphone icon. Use a `surface-tint` (#a43d00) outer glow that pulses to indicate the AI is listening.

---

## 6. Do’s and Don’ts

### Do
*   **Do** use large icons (24px+) accompanied by text. Never rely on icons alone.
*   **Do** use `spacing-8` (2.75rem) or higher for "Breathing Room" between major functional blocks.
*   **Do** ensure that the Hindi translation is given equal visual weight (size and color) as the English text.

### Don’t
*   **Don’t** use pure black (#000000). Use `on-background` (#1a1c1c) for a softer, more premium contrast.
*   **Don’t** use "hairline" strokes or 1px borders. They disappear on low-resolution mobile screens common in rural areas.
*   **Don’t** cram more than three primary actions on a single screen. If it's complex, break it into a stepped "Wizard" flow.
*   **Don’t** use "Center Aligned" text for long paragraphs. Always left-align (or right-align for specific scripts) to maintain a consistent "reading edge."

---

## 7. Spacing & Rhythm

All spacing must follow the **0.7rem increment** (the '2' token).
- **Internal Padding:** `spacing-3` (1rem)
- **Between Sections:** `spacing-6` (2rem)
- **Screen Margins:** `spacing-4` (1.4rem)

This consistent rhythm creates a predictable, "calm" interface that reduces cognitive load for users who may be intimidated by technology.