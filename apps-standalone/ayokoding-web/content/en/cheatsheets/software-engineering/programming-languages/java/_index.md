---
title: 'Java'
date: 2025-03-20T07:16:00+07:00
draft: false
---

# Java Programming Cheatsheets

- [Getting Started with Java](./getting-started/)

## 1. Getting Started with Java

- **Basic Syntax**
  - Comments (single-line, multi-line, documentation)
  - Printing and output streams
  - Variable declarations and naming conventions
  - Primitive data types and their wrappers
  - Operators (arithmetic, relational, logical, bitwise)
  - Type conversion and casting
  - Literals and constants
- **Control Structures**
  - if-else constructs and nested conditions
  - switch statements (traditional and expression-based)
  - Loops (for, enhanced for, while, do-while)
  - Break, continue, and labeled statements
  - Expression blocks and lambda expressions
- **Functions (Methods)**
  - Method definition syntax
  - Return types and void methods
  - Parameter passing (by value)
  - Method overloading rules
  - Varargs parameters
  - Static and instance methods
- **Arrays and Basic Collections**
  - Array creation and initialization
  - Multidimensional arrays
  - Array utility methods
  - ArrayList and basic operations
  - Converting between arrays and collections
- **Input and Output Basics**
  - Console input with Scanner
  - System.out and System.err
  - Basic file reading and writing
  - Buffered I/O for performance
  - Character vs byte streams

## 2. Object-Oriented Programming Fundamentals

- **Classes and Objects**
  - Class definition syntax
  - Object instantiation
  - Constructors (default, parameterized, chaining)
  - Instance variables and methods
  - Static variables and methods
  - Object lifecycle and garbage collection
  - Object identity vs equality
  - toString, equals, and hashCode methods
- **Modifiers and Visibility**
  - Access modifiers (public, protected, default, private)
  - Non-access modifiers (static, final, abstract, transient, volatile)
  - Interface and class visibility
  - Package organization and visibility
- **String Handling**
  - String class core methods
  - String immutability and string pool
  - StringBuilder and StringBuffer
  - String formatting and interpolation
  - Regular expressions with String
  - String performance considerations
- **Error Handling**
  - Exception hierarchy (checked vs unchecked)
  - try-catch-finally blocks
  - Multi-catch and union catch
  - try-with-resources for automatic resource management
  - Throwing and propagating exceptions
  - Creating custom exception classes
  - Exception handling best practices
  - Error vs Exception vs RuntimeException

## 3. Java Development Environment

- **Java Execution Model**
  - Compilation process (source to bytecode)
  - Java Virtual Machine (JVM) architecture
  - Interpretation vs Just-In-Time (JIT) compilation
  - Class loading mechanism
  - Memory management (heap, stack, method area)
  - Garbage collection algorithms and tuning
  - JVM flags and optimization options
- **Command-Line Tools**
  - Compilation with javac (syntax, options, classpath)
  - Running programs with java (syntax, JVM arguments)
  - Creating and using JAR files (jar command)
  - Generating documentation (javadoc)
  - Bytecode analysis (javap)
  - Troubleshooting tools (jps, jstat, jmap, jstack, jconsole)
- **Essential Build Tools**
  - Maven fundamentals (pom.xml structure, dependencies)
  - Maven lifecycles and plugins
  - Gradle basics (build.gradle, Groovy DSL)
  - Dependency management best practices
  - Build automation and profiles
- **Testing with Standard Library**
  - Assertions with the assert keyword
  - Enabling assertions at runtime
  - Writing effective assertion messages
  - Designing testable code
  - Command-line test execution
  - Creating simple test harnesses
  - System.out vs dedicated test reporting

## 4. Advanced Object-Oriented Programming

- **Inheritance and Polymorphism**
  - Extending classes with inheritance
  - Method overriding rules
  - Super keyword and constructor chaining
  - Abstract classes and methods
  - Final classes and methods
  - Virtual method invocation
  - Type casting and instanceof operator
  - Covariant return types
- **Interfaces**
  - Interface definition and implementation
  - Multiple interface inheritance
  - Default and static methods in interfaces
  - Functional interfaces and their applications
  - Interface constants
  - Marker interfaces
- **OOP Principles in Practice**
  - Encapsulation techniques and benefits
  - Proper inheritance design
  - Polymorphic design patterns
  - Abstraction in APIs
  - Composition vs inheritance
  - Designing for extensibility
- **Modern Java Class Features**
  - Records for immutable data (Java 16+)
  - Sealed classes and interfaces (Java 17+)
  - Pattern matching for instanceof (Java 16+)
  - Text blocks for multiline strings (Java 15+)

## 5. Java Standard Library

- **Collections Framework**
  - Collection interface hierarchy
  - Lists (ArrayList, LinkedList, Vector)
  - Sets (HashSet, LinkedHashSet, TreeSet)
  - Maps (HashMap, LinkedHashMap, TreeMap, EnumMap)
  - Queues and Deques (PriorityQueue, ArrayDeque)
  - Collection algorithms (sort, search, shuffle)
  - Comparator and Comparable interfaces
  - Unmodifiable and synchronized wrappers
  - Collection performance characteristics
- **I/O and NIO**
  - Stream-based I/O hierarchy
  - File and directory operations
  - Buffer-oriented I/O with NIO
  - Channels and selectors
  - Memory-mapped files
  - Path operations and file walking
  - Asynchronous I/O
  - Object serialization and externalization
- **Date and Time API**
  - LocalDate, LocalTime, LocalDateTime
  - ZoneId, ZonedDateTime, and OffsetDateTime
  - Instant for machine time
  - Duration and Period
  - Formatting and parsing
  - Date and time calculations
  - Legacy date/time API conversion
- **Utility Classes**
  - Math class operations
  - Random and SecureRandom
  - Regular expressions with Pattern and Matcher
  - Optional for null safety
  - Objects utility methods
  - Base64 encoding/decoding
  - UUID generation and parsing

## 6. Functional Programming in Java

- **Lambda Expressions**
  - Lambda expressions syntax and scoping
  - Method references (static, instance, constructor)
  - Functional interfaces in java.util.function
  - Higher-order functions
- **Functional Programming Concepts**
  - Pure functions and side effects
  - Function composition
  - Currying and partial application
  - Monads (Optional as an example)
  - Lazy evaluation
- **Streams API**
  - Stream creation
  - Intermediate operations (filter, map, flatMap)
  - Terminal operations (collect, reduce, forEach)
  - Collectors utility methods
  - Parallel streams
  - Stream pipeline optimization
  - Custom collectors
  - Infinite streams

## 7. Advanced Java Features

- **Generics**
  - Generic classes and interfaces
  - Type parameters and naming conventions
  - Bounded type parameters (extends, super)
  - Wildcards (? extends, ? super)
  - Generic methods and constructors
  - Type erasure and its implications
  - Raw types and backward compatibility
  - Reifiable vs non-reifiable types
- **Reflection API**
  - Class<?> and Class.forName()
  - Inspecting fields, methods, and constructors
  - Accessing and modifying fields
  - Invoking methods
  - Creating new instances
  - Array reflection
  - Reflection performance considerations
- **Annotations**
  - Built-in annotations (@Override, @Deprecated, etc.)
  - Creating custom annotations
  - Retention policies and targets
  - Annotation processors
  - Type annotations
  - Repeatable annotations
  - Reflection with annotations
- **Dynamic Proxies**
  - Creating proxy instances
  - InvocationHandler implementation
  - Common proxy use cases
  - Limitations of dynamic proxies
  - Bytecode manipulation libraries overview

## 8. Concurrent Programming

- **Thread Basics**
  - Thread creation (extending Thread, implementing Runnable)
  - Thread lifecycle states
  - Thread priorities and daemon threads
  - Thread local variables
  - Thread groups
  - Uncaught exception handlers
- **Synchronization Mechanisms**
  - Race conditions and thread safety
  - Synchronized methods and blocks
  - Lock objects and ReentrantLock
  - ReadWriteLock for concurrent reads
  - Conditions for thread coordination
  - Volatile keyword and happens-before relationship
  - Wait, notify, and notifyAll
- **Concurrent Collections and Utilities**
  - Atomic variables for lock-free operations
  - Concurrent collections (ConcurrentHashMap, CopyOnWriteArrayList)
  - Blocking collections (BlockingQueue variants)
  - ThreadLocal variables and inheritance
  - Barriers (CyclicBarrier, Phaser)
  - Latches (CountDownLatch)
  - Semaphores for resource control
  - Exchangers for data swapping
- **ExecutorService and Asynchronous Programming**
  - Thread pools and executor services
  - Callable, Future, and CompletableFuture
  - Asynchronous programming patterns
  - Timeouts and cancellation
- **Virtual Threads (Java 21+)**
  - Introduction and key concepts
  - Creating and managing virtual threads
  - Structured concurrency
  - Performance characteristics and memory footprint
  - Platform vs. virtual thread comparison
  - Use cases and best practices
  - Limitations and considerations
- **Concurrency Design Patterns**
  - Producer-consumer pattern
  - Master-worker pattern
  - Read-write lock pattern
  - Double-checked locking
  - Immutable objects for thread safety
  - Thread-confinement pattern

## 9. Parallel Programming

- **Parallel Programming Fundamentals**
  - Task parallelism vs. data parallelism
  - Amdahl's Law and scalability considerations
  - Divide-and-conquer strategies
  - Recursive decomposition techniques
  - Work stealing algorithms
  - When to use parallelism (and when not to)
- **Java Parallel Programming Tools**
  - Fork/Join framework architecture
  - RecursiveTask and RecursiveAction
  - Parallel streams processing
  - Spliterators and custom data decomposition
  - Parallel algorithms in Collections
  - Parallel array operations
  - Numerical computation optimization
- **Parallel Design Patterns**
  - Map-reduce pattern
  - Sideshow pattern for parallel event processing
  - Pipeline parallelism
  - Data parallelism techniques

## 10. Modern Java Development

- **Modular Programming**
  - Package structure and naming conventions
  - Java Module System (JPMS) fundamentals
  - module-info.java syntax
  - Exports, requires, uses, and provides
  - Service Provider Interface (SPI) pattern
  - Migration from classpath to modules
  - Multi-release JARs
- **Containerization with Docker**
  - Creating Java-specific Dockerfiles
  - Multi-stage builds for Java applications
  - Docker Compose for multi-container applications
  - Docker volumes for persistent data
  - JVM configuration in containerized environments
  - Container resource limits and JVM memory settings
  - Docker best practices for Java applications
- **CI/CD for Java Projects**
  - Continuous Integration fundamentals
  - Setting up Java projects in CI systems (Jenkins, GitHub Actions, GitLab CI)
  - Automated testing in CI pipelines
  - Code quality tools integration (SonarQube, SpotBugs, PMD)
  - Artifact management (Nexus, Artifactory)
  - Deployment automation strategies
  - Blue-green and canary deployments
- **Cloud-Native Java**
  - Microservices architecture with Java
  - Spring Boot and cloud-native frameworks
  - Configuration management
  - Service discovery patterns
  - API gateway implementation
  - Circuit breakers and bulkheads
  - Monitoring and observability
- **Modern Testing Practices**
  - Test-Driven Development (TDD) workflow
  - Unit testing with JUnit 5 and Mockito
  - Integration testing strategies
  - Performance testing (JMH)
  - Load and stress testing
  - Contract testing
  - End-to-end testing automation
