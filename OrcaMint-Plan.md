# OrcaMint — Planning & Brainstorm Doc

> Living document. Add ideas, cross things out, ask questions. Nothing here is final.

---

## What Is OrcaMint?

The first NFT minting platform built natively on Lightchain. Users connect their Trust Wallet, create digital art (with AIVM's help or by uploading their own), and mint it as an NFT on the Lightchain blockchain — permanently recorded, provably owned.

**The core idea:** Make NFT creation easy enough for someone with zero technical knowledge. You shouldn't need to know what a blockchain is to mint on one.

---

## Why Lightchain / Why Now?

- No NFT tool exists on Lightchain yet — we'd be first
- AIVM makes AI-generated art a native feature, not a bolt-on
- The Ethereum NFT hype bubble has passed, which cleared out scammers — real collectors and artists remain
- Lightchain is growing; getting in early means the ecosystem grows around OrcaMint

---

## Things We Like (Keep These)

- [ ] **Profile page** — banner image + avatar + stats (total value, # items) + tabs: Collected / Created / Listings / Favorites / Activity. Clean and gives everything at a glance. (OpenSea's Keiko326 profile was the reference)
- [ ] **Art origin labels** — every NFT shows how it was made:
  - 🎨 **Artist Upload** — creator brought their own work (photo, drawing, Grok-generated, anything)
  - ⚡ **AIVM Enhanced** — uploaded art processed/modified through Lightchain AIVM
  - 🤖 **AIVM Generated** — created entirely by Lightchain AIVM
  - Prevents misrepresentation; makes the AIVM badge a mark of authenticity for Lightchain-native art
- [ ] **AI art generation via AIVM** — describe what you want in plain English, AIVM makes it ⚠️ SEE CONCERNS BELOW
- [ ] **Countdown drops** — scheduled launch dates with a timer, limited supply, builds excitement (like sneaker drops)
- [ ] **Gallery page** — every wallet gets a page showing everything they've minted, shareable link
- [ ] **Trust Wallet login** — connect wallet = your identity, no account needed
- [ ] **LCAI payments** — mint fee paid in LCAI
- [ ] **Limited supply collections** — "only 500 will ever exist" creates scarcity and value
- [ ] **Unique per wallet** — each mint gets a slightly different AI-generated version
- [ ] **Privacy-first** — no email, no tracking, wallet = identity. Privacy policy is one paragraph, not 10 pages like OpenSea's. This is a real differentiator.
- [ ] **Notifications** — alert users when their NFT sells, when a drop goes live, when they receive an offer. Makes the platform feel alive. (Could tie into OrcaMail for wallet-to-wallet delivery)
- [ ] **Public profiles, no login required** — anyone can browse a profile or collection via a shareable link without connecting a wallet. Wallet only needed to mint/buy/edit. Makes galleries easy to share anywhere.

---

## AIVM Image Generation — Problem & Decision

**Two real problems Keiko identified:**
1. **Speed** — AIVM on-chain inference is slow (30-60+ seconds per image). Bad UX if user is waiting.
2. **Quality/detail** — AIVM text models aren't dedicated image generators. Output can be rough compared to Midjourney/DALL-E.

**Options discussed:**
- Queue it (user submits, gets notified when done — like Midjourney) — solves speed UX but not quality
- Use ComfyUI/FLUX for images (already running for OrcaArt), AIVM for metadata only — fast + quality
- Let users upload their own art — no generation needed, AIVM helps with description/tags/title
- All three options available at once

**Decision: Option 3 — Upload your own image. AIVM handles text only.**

- User uploads their own art (photo, drawing, digital painting, anything)
- AIVM writes the description, suggests tags, generates a title if they want help
- No waiting on image generation — upload is instant
- Real artists bring real art — better quality, better first impressions
- AI image generation (AIVM or ComfyUI) added later as a bonus feature once we know quality is good enough

---

## Things We're Not Sure About

- [ ] **Open studio vs. curated drops** — should anyone be able to mint anything, or should collections be approved/curated?
- [ ] **Phase 1 minting only vs. Phase 2 marketplace** — buying & selling between users requires a smart contract escrow; do we launch simple and add trading later?
- [ ] **Free minting vs. paid** — charge a flat LCAI fee per mint? Or let creator set the price?
- [ ] **Royalties** — original creator earns a % every time their NFT resells (common on OpenSea). Worth building from the start?

---

## Things We Don't Like / Want to Avoid

- [ ] Complexity — if it takes more than 3 clicks to mint, it's too hard
- [ ] Anything that requires users to understand blockchain to use it
- [ ] Cloud storage of art on our server (user privacy principle — we don't store their data)
- [ ] Gas fee surprises — user should know exactly what it costs before they confirm
- [ ] Scam/spam NFT clutter — OpenSea profiles get flooded with airdropped junk NFTs. OrcaMint should have a Hide/Report button from day one so profiles stay clean. (Keiko saw EVMKER VOUCHER and EVMNET VOUCHER scam NFTs in her own profile as an example)

---

## Pricing Model

| Action | Cost | Who pays | Goes to |
|--------|------|----------|---------|
| Join / create account | Free | — | — |
| Mint an NFT | ~1–2 LCAI flat fee | Minter | OrcaMint wallet (covers gas) |
| Deploy a collection / drop | ~5–10 LCAI flat fee | Creator | OrcaMint wallet (covers contract gas) |
| Sell an NFT | 2.5% of sale price | Seller | OrcaMint wallet |
| Resale royalty | 0–10% (creator sets it) | Buyer | Original creator's wallet — automatic |
| Swap LCAI | Not our feature | — | Link to Lightchain SWAP |

**Revenue model:** Mint fees + 2.5% commission on every sale. Scales with usage. Simple and fair.

**Notes:**
- Royalties are set by the creator at mint time and paid automatically forever — one of the most valuable things about NFTs for artists
- "Lazy minting" (free to create, gas charged only on first sale) is a Phase 2 option to lower the barrier further
- 2.5% is the OpenSea standard rate; since OrcaMint is the only NFT platform on Lightchain there's no price competition to worry about at launch

---

## Technical Decisions (Locked)

| Component | Decision | Why |
|-----------|----------|-----|
| Frontend hosting | **Cloudflare Pages** | Free, fast CDN, auto-deploy from GitHub, proven with OrcaFiles |
| Image storage | **Cloudflare R2** | Free tier 10GB + 1M requests/month; $0.015/GB after. Cheap, fast, reliable. Images get permanent URL stored in NFT metadata on Lightchain. |
| AIVM calls | **Railway CORS proxy** (already running) | Same fix as OrcaFiles — routes through web-production-0ccfe.up.railway.app |
| Wallet/minting | **Trust Wallet via window.ethereum** | All contract calls go through wallet — no CORS issues |
| Domain | **orcamint.art or orcamint.xyz** | .ai too expensive (~$100/yr). .art is thematic for NFT platform (~$12/yr). .xyz is proven (we use .xyz already, ~$10/yr). Grab before someone squats on it. |

---

## Open Questions

1. **Who is the target user?** Artists? Collectors? Lightchain community? General public?
2. **Should OrcaMint have its own collections** (like "OrcaWhales — 500 unique orcas") or only host other people's drops?
3. **Do we want a trading/resale marketplace eventually, or just minting?**

---

## Possible Phases

### Phase 1 — Mint (Build This First)
- Connect wallet
- Create art: describe it → AIVM generates → or upload your own image
- Name it, write a description, set quantity (1 of 1 or part of a collection)
- Mint → pay LCAI fee → NFT recorded on Lightchain
- Personal gallery page with shareable link

### Phase 2 — Drops
- Creator builds a themed collection
- Sets a launch date + countdown page
- Sets mint price in LCAI and max supply
- Community mints on drop day; sold out = sold out

### Phase 3 — Marketplace (Later)
- Buy and sell NFTs between wallets
- Creator earns royalty on every resale
- Browse all collections, trending items, recent sales

---

## Inspiration / Reference

- **OpenSea** (opensea.io) — largest NFT marketplace on Ethereum. Good reference for marketplace UI
- **The GhOsts** — example of a curated drop with countdown timer. Clean, focused minting page
- **Bored Ape Yacht Club** — example of a limited collection (10,000 items) with community identity
- **CryptoPunks** — original 10,000 pixel-art NFTs; still the gold standard for scarcity/value

---

## OpenSea UI Observations (things worth stealing)

Keiko explored OpenSea on 2026-05-27. Things she liked and noted:

### Navigation / Sidebar (like this layout)
- Clean dark sidebar with icons + labels
- Top sections: Discover, Collections, Tokens, Swap, **Drops**, Activity, Rewards, **Studio**
- Settings expands to show: Profile, Linked Wallets, Notifications, Customize, Developer, Verification, Shortcuts
- Very organized — creator tools (Studio) are separate from browsing (Discover/Collections)
- **For OrcaMint:** We could borrow this exact structure — Browse | Drops | Studio | My Collection | Settings

### Swap Page
- OpenSea has a built-in token swap. Clean from/to interface, shows price and slippage.
- Lightchain already has its own SWAP — we don't need to build this, but worth noting they combined it all in one place
- **For OrcaMint:** Could link to Lightchain SWAP for users who need LCAI to mint

### Deploy Collection Contract (Studio flow)
- Simple form: upload collection image, enter contract name, token symbol, pick chain
- Chain picker shows Ethereum and ERC1155 options — for OrcaMint this would just say "Lightchain"
- That's literally all you need to start a collection — 3 fields and a button
- **For OrcaMint:** This is our Studio flow. We can match this simplicity exactly.

### Trending / Analytics Page
- Shows all collections with: floor price, 24h volume change (% green/red), top offer, # listed, # owners, # sales, sales chart sparkline
- Very data-rich but still readable
- **For OrcaMint Phase 3:** This is what the marketplace browse page looks like when you have trading volume

### Networks OpenSea Supports
- Ethereum, Abstract, AnimeChain, ApeChain, Arbitrum, Avalanche, Base, Berachain, Blast, Flow, HyperEVM, Hyperliquid, Monad, Optimism, Polygon, Ronin, Sei, Somnia, and many more
- **Lightchain is NOT on this list** — OpenSea has no Lightchain support
- This confirms OrcaMint has zero competition on Lightchain from the biggest player in the space

### Liquidity Sources OpenSea Uses
- OpenSea, Uniswap, Orca, Raydium, PancakeSwap, Aerodrome, FOMO, Pumpfun, Meteora, MetaMask, Blur, CryptoPunks, and more
- All "Active" — OpenSea aggregates liquidity from many sources
- **For OrcaMint:** We don't need this complexity at launch; it's a Phase 3+ feature

### Support Widget (really like this)
- Floating help button that opens a chat panel — "Hi there 👋 How can we help?"
- Shows AI Agent + human team option
- Has pre-built FAQ questions: "How do I create an NFT?", "How do I sell an NFT?", "What are some common web3 scams?"
- Bottom tabs: Home | Messages | Help
- The NFT avatars at the top are a nice touch — shows what the product is about immediately
- **For OrcaMint:** This is much better than our current Tally form approach. Build a support widget like this — AI-powered (AIVM), with a few common questions pre-loaded. Could reuse the OrcaMail pattern for the "message the team" part.

---

## Notes & Random Ideas

- OrcaMint could be the place where Lightchain community identity forms — like how BAYC owners use their ape as their profile picture everywhere
- Could tie into OrcaMail — send an NFT directly to someone's wallet as a message attachment?
- Could tie into OrcaLearn — student achievement badges as NFTs?
- AIVM angle is the story: "AI-generated art, minted on the chain that powers that AI" — no other platform can say that
- The support widget with AI + FAQ is a much better help experience than a Tally form — consider this pattern for ALL future apps

---

*Last updated: May 27, 2026*
