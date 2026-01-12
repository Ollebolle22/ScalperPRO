# ⚡ Fast Momentum Scalper 1M

En snabb och enkel momentum-baserad scalper strategi för 1-minuters timeframe.

## 📋 Översikt

Denna strategi är designad för snabb scalping på 1-minuters chart med fokus på momentum-förändringar. Till skillnad från de mer komplexa 15-minuters strategierna är detta en **ren scalper** utan DCA eller komplicerade take profit-nivåer.

### ✨ Huvudfunktioner

- ✅ **1-minuters timeframe** - Snabba in och ut
- ✅ **Momentum-baserad** - RSI + EMA crossovers
- ✅ **Enkel risk management** - En stoploss, en takeprofit
- ✅ **Ingen DCA** - Ren scalping utan averaging
- ✅ **WunderTrading integration** - Fullständig bot support
- ✅ **Live dashboard** - Realtidsstatistik på chartet

## 🎯 Strategi Logic

### Entry Conditions (LONG)

Alla följande måste vara uppfyllda:

1. **EMA Crossover**: EMA 9 korsar över EMA 21
2. **Bullish Momentum**: RSI > 50 och stigande
3. **Trend Alignment**: Pris över EMA 50 (trend filter)
4. **Trend Strength**: ADX ≥ 20 (undviker ranging markets)
5. **Volume Confirmation**: Volume > 1.2x moving average

### Entry Conditions (SHORT)

Motsatta villkor för short-positioner.

### Exit Strategy

**Enkel och direkt:**
- **Stop Loss**: 1.5 x ATR under entry (för longs)
- **Take Profit**: 2.5 x ATR över entry (för longs)
- **Risk/Reward Ratio**: 1:1.67

Inga trailing stops, inga breakeven-moves, inga partial exits. När du är i en trade så kör du den till antingen SL eller TP.

## 📊 Indikatorer

### EMA (Exponential Moving Average)
- **EMA 9** (gul) - Snabb momentum
- **EMA 21** (orange) - Trend confirmation
- **EMA 50** (blå) - Overall trend filter

### RSI (Relative Strength Index)
- **Period**: 14
- **Threshold**: 50 (neutral)
- Används för momentum-riktning (stigande/fallande)

### ADX (Average Directional Index)
- **Period**: 14
- **Minimum**: 20
- Filtrerar ut ranging markets (choppy movement)

### ATR (Average True Range)
- **Period**: 14
- Används för att beräkna SL/TP baserat på volatilitet

### Volume
- **MA Period**: 20
- **Multiplier**: 1.2x
- Kräver 20% högre volume än genomsnitt

## ⚙️ Inställningar

### 💰 Kapital & Leverage

```
Leverage: 5.0x (1x - 20x)
Position Size: 95% av equity
```

**Tips**: För 1-minuters scalping är 5x leverage bra. Högre leverage = högre risk på snabba moves.

### 🎯 Risk Management

```
Stop Loss: 1.5 x ATR (0.5 - 3.0)
Take Profit: 2.5 x ATR (1.0 - 5.0)
```

**Tips**:
- Tight SL (1.0-1.5 ATR) för snabba exits på 1min
- TP (2.0-3.0 ATR) för realistiska targets

### 📈 EMA Settings

```
EMA Fast: 9 (snabbare än 21 för 1min)
EMA Slow: 21
EMA Trend: 50
```

### 🎯 RSI Settings

```
RSI Period: 14
Momentum Threshold: 50
```

### 💪 ADX Settings

```
ADX Period: 14
Minimum Threshold: 20
```

**Tips**: Sänk ADX till 15-18 för fler trades, höj till 22-25 för färre men starkare signaler.

### 📦 Volume Filter

```
Volume Multiplier: 1.2x
Volume MA Period: 20
```

## 🤖 WunderTrading Setup

### 1. Konfigurera Bot Settings i TradingView

```
Bot ID: your_bot_id_here (från WunderTrading)
Exchange: HyperLiquid / Binance / Bybit / OKX
Trading Pair: SOL-USDC (eller din pair)
Strategy Name: FMS_1M (kort namn)
```

### 2. Alert Format

Strategin genererar automatiskt korrekt JSON för WunderTrading:

**Entry Alert:**
```json
{
  "code": "ENTER-LONG_HyperLiquid_SOL-USDC_FMS_1M_your_bot_id",
  "orderType": "market",
  "amountPerTrade": 1.5,
  "amountPerTradeType": "contracts",
  "leverage": 5.0,
  "stopLoss": {"price": 135.00},
  "takeProfit": {"price": 145.00},
  "reduceOnly": false,
  "placeConditionalOrdersOnExchange": false
}
```

**Exit Alert:**
```json
{
  "code": "EXIT-LONG_HyperLiquid_SOL-USDC_FMS_1M_your_bot_id",
  "amountPerTrade": 1.5,
  "amountPerTradeType": "contracts",
  "reduceOnly": true,
  "placeConditionalOrdersOnExchange": false
}
```

### 3. Skapa Alert i TradingView

1. Lägg till strategin på 1-minuters chart
2. Klicka på "Alert" (klockan)
3. **Condition**: Välj strategins namn
4. **Webhook URL**: `https://wtalerts.com/bot/trading_view`
5. **Message**: Lämna tom (strategin sätter alert_message automatiskt)
6. **Notifications**: Aktivera "Webhook URL"
7. Klicka "Create"

## 📈 Förväntade Resultat

### 1-minuters Timeframe Characteristics

- **Antal trades**: 10-30 per dag (beroende på volatilitet)
- **Win rate**: 40-55% (scalping har lägre win rate men bättre R:R)
- **Risk/Reward**: 1:1.67 per trade
- **Hold time**: 2-15 minuter i genomsnitt

### Optimala Marknadsförhållanden

- ✅ **Trending markets** - Stark riktning (ADX > 20)
- ✅ **High volume** - Aktiv trading
- ✅ **Volatilitet** - Tillräcklig rörelse för SL/TP
- ❌ **Ranging markets** - ADX filter hjälper här
- ❌ **Low volume** - Strategin skippar dessa

## 🎨 Visual Elements

### On-Chart
- **Gul linje**: EMA 9 (snabb)
- **Orange linje**: EMA 21 (slow)
- **Blå linje**: EMA 50 (trend)
- **Grön triangel**: LONG entry signal
- **Röd triangel**: SHORT entry signal
- **Background**: Grön/röd nyans för trend direction

### Dashboard (Top Right)
Visar live:
- RSI nivå (färgkodad)
- ADX styrka
- ATR volatilitet
- Volume status (OK/NOT OK)
- Trend (BULL/BEAR)
- Position (LONG/SHORT/NONE)
- Open P&L %
- Win Rate %
- Total antal trades

## ⚠️ Viktiga Påminnelser

### För 1-minuters Scalping

1. **Snabb execution är kritisk** - Använd alltid market orders
2. **Kommission spelar stor roll** - 0.06% är satt som default
3. **Slippage händer** - 2 ticks är satt som default
4. **Många trades = många fees** - Räkna med att fees äter profit
5. **Inte för alla marknader** - Fungerar bäst på stora liquid pairs

### Rekommenderade Pairs

- **SOL/USDC** - Hög volatilitet, bra för scalping
- **ETH/USDC** - Liquid och stabil
- **BTC/USDC** - Mindre volatilitet men mycket liquid
- **Undvik** - Low volume altcoins på 1min

### Risk Warnings

- 🔴 **1-minuters scalping är intensivt** - Många trades, snabba rörelser
- 🔴 **Högre leverage = högre risk** - En bad streak kan tömma kontot snabbt
- 🔴 **Backtesta först** - Kör på historisk data innan live
- 🔴 **Paper trade först** - Testa med fake money först

## 🔧 Felsökning

### Problem: Inga trades körs

**Möjliga orsaker:**
1. ADX < 20 (marknaden är ranging)
2. Volume för låg
3. Inga EMA crossovers (marknaden är sideways)
4. Redan i position (pyramiding = 0)

**Lösning:**
- Sänk ADX threshold till 15-18
- Sänk volume multiplier till 1.0-1.1
- Vänta på trending market

### Problem: För många trades (overtrading)

**Lösning:**
- Höj ADX threshold till 22-25
- Höj volume multiplier till 1.3-1.5
- Använd längre EMA perioder (11/26 istället för 9/21)

### Problem: Många stop losses

**Möjliga orsaker:**
1. SL för tight (< 1.0 ATR)
2. För choppy market (låg ADX ändå släpper trades igenom)
3. Slippage på 1min är större än förväntat

**Lösning:**
- Öka SL till 2.0 ATR
- Höj ADX minimum till 25
- Testa på 3min eller 5min istället

## 📊 Backtesting Tips

### TradingView Backtester

1. Lägg strategin på 1-minuters chart
2. Välj tillräckligt lång historik (3-6 månader)
3. Kontrollera:
   - **Max Drawdown** (bör vara < 20%)
   - **Win Rate** (40-55% är OK för scalping)
   - **Profit Factor** (> 1.5 är bra)
   - **Antal trades** (för få = för restriktiva filters)

### Viktiga Metrics

- **Sharp Ratio** > 1.0
- **Max Consecutive Losses** < 8
- **Average Trade Duration** < 20 min för scalping

## 🚀 Nästa Steg

1. **Importera** filen till TradingView
2. **Lägg på 1min chart** för ditt trading pair
3. **Justera settings** baserat på pair characteristics
4. **Backtest** på 3-6 månaders historik
5. **Paper trade** i minst 1 vecka
6. **Gå live** med litet kapital först ($100-500)
7. **Skala upp** när strategin är profitable

## 📞 Support & Feedback

Om du hittar bugs eller vill föreslå förbättringar, öppna ett issue på GitHub:
https://github.com/Ollebolle22/ScalperPRO/issues

---

**Lycka till med din scalping! 🚀**

*Remember: Past performance does not guarantee future results. Trade responsibly.*
