# 📊 Observability in Google ADK

Observability is a **core principle** when developing agents with the Google Agent Development Kit (ADK). It enables developers to **monitor, debug, and optimize** agents with transparency and confidence.

This guide introduces two key approaches:

1. **Agent Observability with Phoenix** – tracing, metrics, and visualization
2. **Logging in the ADK** – structured logs for debugging and monitoring

---

## 🎯 What You'll Learn

* **Phoenix Observability**: How to enable and use Phoenix to track agent behavior
* **ADK Logging**: Configuring and using built-in logging features
* **Best Practices**: Strategies for debugging and monitoring agents in production
* **Limitations**: Understanding the scope and boundaries of observability tools

---

## 🧠 Core Concept: Observability

Observability in ADK provides:

* **Transparency**: Track how your agent processes inputs and calls tools
* **Debugging**: Understand errors and unexpected behaviors
* **Performance Monitoring**: Measure latency, execution flow, and tool usage
* **Operational Insight**: Ensure your agent is production-ready

---

### Important Limitations

* ⚠️ **Configuration Required**: Phoenix needs setup for metrics collection
* ⚠️ **Logging Scope**: Logs capture runtime events but not full execution graphs
* ⚠️ **Performance Impact**: Excessive observability can add overhead in high-traffic environments

---

## 🔧 Observability Tools in ADK

### 1. **Phoenix Integration**

* **Purpose**: Provides deep observability into agent workflows
* **Use Cases**: Debugging tool execution, tracing agent decisions, monitoring latency
* **Benefits**: Rich visualization, structured traces, performance metrics

[For more info: Use this link](https://google.github.io/adk-docs/observability/phoenix/)

---

### 2. **ADK Logging**

* **Purpose**: Capture structured logs for debugging and monitoring
* **Use Cases**: Error detection, runtime insights, auditing tool usage
* **Benefits**: Lightweight, flexible, easy to integrate with log aggregators

[For more info: Use this link](https://google.github.io/adk-docs/observability/logging/)

---

## 🚀 Tutorial Examples

This sub-example includes two practical implementations:

### **Phoenix-Enabled Agent**

**Location**: `./phoenix_observable_agent/`

* Captures traces of agent runs
* Exports metrics for visualization
* Demonstrates workflow debugging with Phoenix

![Example](/screenshots/phoenix_observability.png)

---

### 📍 **Logging Agent**

**Location**: `./logging_agent/`

* Implements structured logging with ADK
* Uses python's standard logging module to provide flexible and powerful logging capabilities
* Logs inputs, outputs, and error events
* Shows integration with external log systems

![Example](/screenshots/debug_logging.png)

---

## 📁 Project Structure

```
adk_observability/
├── README.md                          # This file - observability guide
├── phoenix_observable_agent/          # Phoenix integration example
│   ├── __init__.py
│   ├── agent.py                       # Agent with Phoenix observability
├── logging_agent/                     # Logging example
│   ├── __init__.py
│   ├── agent.py                       # Agent with structured logging
└── requirements.txt                   # Dependencies for observability
└── .example.env                       # Example configuration for Phoenix/logging
```

---

## 🚀 Getting Started

1. **Set up your environment**:

   ```bash
   cd adk_observability

   # Copy the environment template
   cp .example.env .env

   # Edit .env and configure Phoenix/logging settings
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the agents**:

   ```bash
   # Start the ADK web interface
   adk web

   # In the interface, select:
   # - phoenix_observable_agent: To test Phoenix observability
   # - logging_agent: To test ADK logging
   ```

---

## 💡 Pro Tips

* **Use Phoenix for Complex Debugging**: Great for tracing multi-step workflows
* **Enable Logging in Production**: Lightweight way to capture runtime issues
* **Balance Observability and Performance**: More metrics/logs = more overhead
* **Integrate with Monitoring Tools**: Export logs/metrics to systems like Stackdriver or Prometheus

---

## 🔧 Common Use Cases

### Phoenix Applications

* **Workflow Tracing**: Visualize how your agent uses tools
* **Latency Monitoring**: Identify bottlenecks in execution
* **Debugging**: Step through agent behavior with trace data

### Logging Applications

* **Error Tracking**: Identify failures in real-time
* **Auditing**: Record agent interactions for compliance
* **Runtime Insights**: Monitor input/output patterns

---

## 🚨 Important Notes

* **Setup Required**: Phoenix requires configuration for full functionality
* **Performance Impact**: Logging and tracing add overhead—monitor usage carefully
* **Production Ready**: Both Phoenix and ADK logging can be integrated with enterprise monitoring systems

---
