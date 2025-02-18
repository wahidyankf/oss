---
title: 'Clojure CLI'
date: 2025-02-18T18:23::04
draft: false
---

# Clojure CLI

```bash
clj -X hello/run
```

- Executes a Clojure program and invokes explicitly the **`run`** function within the **`hello`** namespace. The purpose and behavior of the **`run`** function would depend on the implementation of the Clojure program you are working with.

```bash
clj -X:deps find-versions :lib clojure.java-time/clojure.java-time
```

- When you run this command, the **`clj`** tooling will search for the available versions of the **`clojure.java-time`** library in the configured repositories and display the results. This can be helpful when you want to check the available versions of a library before specifying the version in your project's dependencies.

```bash
clj -Sdeps '{:deps {nrepl/nrepl {:mvn/version "1.0.0"}}}' -m nrepl.cmdline -c --host 127.0.0.1 --port 55499
```

- Breakdown:
  - `clj`: This is the command-line tool for running Clojure programs.
  - `Sdeps '{:deps {nrepl/nrepl {:mvn/version "1.0.0"}}}'`: This option specifies the dependencies for the Clojure program. In this case, it sets the dependency for `nrepl/nrepl` library with a specific version of "1.0.0". The `Sdeps` option is used to configure the dependencies before launching the program.
  - `m nrepl.cmdline`: This part of the command specifies the namespace `nrepl.cmdline` to be executed. This namespace provides the command-line interface for running an nREPL server.
  - `c`: This option instructs the nREPL server to start in "headless" mode, which means it doesn't launch a REPL session automatically. Instead, it waits for connections from clients.
  - `-host 127.0.0.1`: This option sets the host IP address for the nREPL server. In this case, it's set to `127.0.0.1`, which represents the loopback address or localhost.
  - `-port 55499`: This option sets the port number on which the nREPL server listens for client connections. In this case, it's set to `55499`, but you can choose a different port number if needed.
  - When you run this command, the `clj` tooling will start an nREPL server with the specified configurations. The nREPL server will be listening for connections on the specified host and port. Clients can connect to this server using nREPL-compatible tools to interact with the running Clojure program.

```bash
clj -Sdeps '{:deps {nrepl/nrepl {:mvn/version "1.0.0"}}}' -m nrepl.cmdline -c --host 127.0.0.1 --port `< .nrepl-port`
```

- When you run this command, the **`clj`** tooling will start an nREPL server with the specified configurations. The port number for the server will be read from the **`.nrepl-port`** file. The nREPL server will listen for client connections on the specified host and port, and clients can connect to it using nREPL-compatible tools to interact with the running Clojure program.
