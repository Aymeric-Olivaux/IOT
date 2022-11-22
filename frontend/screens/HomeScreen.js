import { Dimensions, StyleSheet, View } from "react-native";
import React, { useLayoutEffect, useState } from "react";
import { LineChart } from "react-native-chart-kit";
import { Picker } from "@react-native-picker/picker";
import { Button, Text } from "react-native-elements";

const linedata = {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [
        {
            data: [20, 45, 28, 80, 99, 43],
            strokeWidth: 2, // optional
        },
    ],
};

const HomeScreen = ({ navigation }) => {
    const [selectedDB, setSelectedDB] = useState();
    const decibel = [];
    for (let i = 100; i >= 30; i--) {
        decibel.push(i);
    }

    useLayoutEffect(() => {
        navigation.setOptions({
            headerBackTitle: "Logout",
        });
    }, [navigation]);
    return (
        <View>
            <LineChart
                data={linedata}
                width={Dimensions.get("window").width} // from react-native
                height={220}
                yAxisLabel={"$"}
                chartConfig={{
                    backgroundColor: "#e84e48",
                    backgroundGradientFrom: "#e84e48",
                    backgroundGradientTo: "#f8b195",
                    decimalPlaces: 2, // optional, defaults to 2dp
                    color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
                    style: {
                        borderRadius: 16,
                    },
                }}
                bezier
                style={{
                    marginVertical: 8,
                    borderRadius: 16,
                }}
            />
            <View style={styles.selections}>
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#e84e48" }}
                    title="Minute"
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#e84e48" }}
                    title="Hour"
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#e84e48" }}
                    title="Day"
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#e84e48" }}
                    title="Week"
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#e84e48" }}
                    title="Month"
                />
            </View>

            <Text h4 style={styles.title}>
                {" "}
                Please select the allowed decibel level{" "}
            </Text>

            <Picker
                selectedValue={selectedDB}
                onValueChange={(itemValue, itemIndex) =>
                    setSelectedDB(itemValue)
                }
                style={styles.picker}
            >
                {decibel.map((db, i) => (
                    <Picker.Item
                        key={i}
                        label={db.toString() + " dB"}
                        value={db}
                    />
                ))}
            </Picker>
        </View>
    );
};

export default HomeScreen;

const styles = StyleSheet.create({
    selections: {
        flexDirection: "row",
        justifyContent: "space-around",
    },
    buttons: {
        width: 75,
    },
    title: {
        textAlign: "center",
        marginTop: 20,
    },
    picker: {
        height: 50,
        width: 150,
        alignSelf: "center",
        marginTop: 20,
    },
});
