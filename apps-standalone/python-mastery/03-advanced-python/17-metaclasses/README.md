# Python Metaclasses Demo

This comprehensive demonstration covers:

1. Basic metaclass creation
2. Class registration patterns
3. Field validation
4. Practical use cases

## Key Features Demonstrated

### Basic Metaclass

- Creating custom metaclasses
- Intercepting class creation
- `__new__` method usage

### Registry Pattern

- Automatic class registration
- Plugin system implementation
- Framework design

### Validation Metaclass

- Field name validation
- Runtime class checks
- Error handling

## How to Run

1. Execute the demo script:
   ```bash
   python main.py
   ```
2. Observe the output demonstrating:
   - Metaclass creation process
   - Automatic class registration
   - Field validation
3. Experiment by:
   - Adding new metaclass features
   - Creating additional validated classes
   - Extending the registry system

## Sample Output

```
Creating class BasicClass with metaclass SimpleMeta
=== PYTHON METACLASSES DEMO ===

BasicClass was created with SimpleMeta
Type of BasicClass: <class '__main__.SimpleMeta'>
Type of BasicClass instance: <class '__main__.BasicClass'>

Registered classes: {'PluginBase': <class '__main__.PluginBase'>, 'PluginA': <class '__main__.PluginA'>, 'PluginB': <class '__main__.PluginB'>}
PluginA type: <class '__main__.RegistryMeta'>
PluginB type: <class '__main__.RegistryMeta'>

ValidatedModel created successfully with valid_field
Validation error: Field 'InvalidField' must be lowercase

=== DEMO COMPLETE ===
Key Takeaways:
- Metaclasses control class creation
- Useful for frameworks and validation
- type is the default metaclass
- Use sparingly as they add complexity
```

## Key Observations

1. Metaclasses intercept class creation before instances are made
2. Each metaclass call creates a new class object
3. The registry pattern shows practical framework use
4. Validation happens at class definition time

## Learning Outcomes

After completing this demo, you will understand:

- How metaclasses control class creation
- Practical applications of metaclasses
- The relationship between classes and metaclasses
- When to use (and not use) metaclasses
