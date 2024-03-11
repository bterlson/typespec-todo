# Prerequisites
- Java 8 or above
- Maven 3.0 or above

## Dependency on Todo SDK

The Todo sample depends on the Todo SDK. The Todo SDK is not available in Maven Central. You need to build the Todo SDK 
and install it into your local Maven repository. To do this, please run the following command in the Todo SDK folder (../tsp-output/java):

```bash
mvn clean install
```
This will add the dependency jar to your local .m2 repository.

# Compile the Todo sample

Run the following maven command to compile the sample:

```bash
mvn clean package
```
This should create a `todosample-1.0.0-beta.1.jar` file in the target folder.

# Run the sample

```bash
java -jar target/todosample-1.0.0-beta.1.jar
```