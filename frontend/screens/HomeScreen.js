import { Dimensions, StyleSheet, View } from "react-native";
import React, { useLayoutEffect, useState, useEffect } from "react";
import { LineChart } from "react-native-chart-kit";
import { Picker } from "@react-native-picker/picker";
import { Button, Text, Image, Input } from "react-native-elements";

const { width } = Dimensions.get("window");

const linedata = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
        {
            data: [20, 45, 28, 80, 99, 43, 50],
            strokeWidth: 2, // optional
        },
    ],
};

const HomeScreen = ({ navigation }) => {
    const [selectedDB, setSelectedDB] = useState(0);
    const [chartData, setchartData] = useState(linedata);
    const [time, setTime] = useState("minute");
    const [email, setEmail] = useState("");

    async function sendReport(mail) {
        const endpoint = "https://backend.ambizen.tryhard.fr/report/1/";
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: mail,
            }),
        });
        console.log(response);
        if (response.status != 200) {
            alert("Error while sending report");
        }
    }

    async function getTime() {
        const endpoint = "https://backend.ambizen.tryhard.fr/data/1/" + time;
        const response = await fetch(endpoint).then((response) =>
            response.json()
        );

        setchartData({
            labels: response.time,
            datasets: [
                {
                    data: response.decibels,
                    strokeWidth: 2, // optional
                },
            ],
        });
    }

    async function getDecibel() {
        const endpoint = "https://backend.ambizen.tryhard.fr/config/1";
        const response = await fetch(endpoint).then((response) =>
            response.json()
        );
        setSelectedDB(response.threshold);
    }

    getDecibel();

    async function sendDecibel(value) {
        const endpoint = "https://backend.ambizen.tryhard.fr/config/1";
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                threshold: value,
            }),
        });
        console.log(response);
        if (response.status != 200) {
            alert("Error while sending decibel");
        }
    }

    const decibel = [];
    for (let i = 150; i >= 30; i--) {
        decibel.push(i);
    }

    useLayoutEffect(() => {
        navigation.setOptions({
            headerBackTitle: "Logout",
        });
    }, [navigation]);

    useEffect(() => {
        getTime();
        // set interval to get data every 5 seconds
        const interval = setInterval(() => {
            getTime();
        }, 5000);
        return () => clearInterval(interval);
    }, [time]);

    return (
        <View>
            <LineChart
                data={chartData}
                width={Dimensions.get("window").width} // from react-native
                height={220}
                yAxisSuffix={" dB"}
                chartConfig={{
                    backgroundColor: "#93C157",
                    backgroundGradientFrom: "#93C157",
                    backgroundGradientTo: "#52ae6d",
                    decimalPlaces: 2, // optional, defaults to 2dp
                    color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
                    style: {
                        borderRadius: 8,
                    },
                }}
                bezier
                style={{
                    borderRadius: 8,
                    margin: 10,
                }}
            />
            <View style={styles.selections}>
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Minute"
                    onPress={() => setTime("minute")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Hour"
                    onPress={() => setTime("hour")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Day"
                    onPress={() => setTime("day")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Week"
                    onPress={() => setTime("week")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Month"
                    onPress={() => setTime("month")}
                />
            </View>

            <Text h4 style={styles.title}>
                {" "}
                Please select the allowed decibel level{" "}
            </Text>

            <Picker
                selectedValue={selectedDB}
                onValueChange={(itemValue, itemIndex) => {
                    setSelectedDB(itemValue);
                    sendDecibel(itemValue);
                }}
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
            <View>
                <View style={styles.health_container}>
                    <Text h4 style={styles.title}>
                        Backend status
                    </Text>
                    <View style={styles.health}>
                        <Image
                            source={{
                                uri: "https://gatus.alexisboissiere.fr/api/v1/endpoints/sigl---tryhard_iot---ambizen-api/health/badge.svg",
                            }}
                            style={{ width: 88, height: 20, margin: 5 }}
                        />
                        <Image
                            source={{
                                uri: "https://gatus.alexisboissiere.fr/api/v1/endpoints/sigl---tryhard_iot---ambizen-api/uptimes/1h/badge.svg",
                            }}
                            style={{ width: 121, height: 20, margin: 5 }}
                        />
                        <Image
                            source={{
                                uri: "https://gatus.alexisboissiere.fr/api/v1/endpoints/sigl---tryhard_iot---ambizen-api/uptimes/7d/badge.svg",
                            }}
                            style={{ width: 121, height: 20, margin: 5 }}
                        />
                    </View>
                </View>
                <View style={styles.health_container}>
                    <Text h4 style={styles.title}>
                        Ambizen status
                    </Text>
                    <View style={styles.health}>
                        <Image
                            source={{
                                uri: "https://gatus.alexisboissiere.fr/api/v1/endpoints/sigl---tryhard_iot---ambizen-device-1/health/badge.svg",
                            }}
                            style={{ width: 88, height: 20, margin: 5 }}
                        />
                        <Image
                            source={{
                                uri: "https://gatus.alexisboissiere.fr/api/v1/endpoints/sigl---tryhard_iot---ambizen-device-1/uptimes/1h/badge.svg",
                            }}
                            style={{ width: 121, height: 20, margin: 5 }}
                        />
                        <Image
                            source={{
                                uri: "https://gatus.alexisboissiere.fr/api/v1/endpoints/sigl---tryhard_iot---ambizen-device-1/uptimes/7d/badge.svg",
                            }}
                            style={{ width: 121, height: 20, margin: 5 }}
                        />
                    </View>
                </View>
            </View>
            <View style={styles.health}>
                <Input
                    style={styles.input}
                    placeholder="Email"
                    autofocus
                    type="email"
                    value={email}
                    onChangeText={(text) => setEmail(text)}
                />
                <Button
                    style={styles.button_sendreport}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Send Report"
                    onPress={() => sendReport(email)}
                />
            </View>
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
    health: {
        flexDirection: "row",
        justifyContent: "space-around",
        alignSelf: "center",
        marginTop: 20,
    },
    health_container: {
        borderColor: "#93C157",
        borderWidth: 2,
        borderRadius: 8,
        margin: 10,
        width: width > 600 ? "30%" : "95%",
        alignSelf: "center",
    },
    button_sendreport: {
        width: 150,
    },
    input: {
        width: 50,
    },
});
