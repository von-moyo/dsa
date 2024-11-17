// function videoCache(videoLogs: [string, number][][], window: number): string[] {
//     const result: string[] = [];
//     const n = videoLogs.length;

//     for (let i = 0; i <= n - window; i++) {
//         const viewCount: { [key: string]: number } = {};

//         // Sum up the views for the current window
//         for (let j = i; j < i + window; j++) {
//             for (const [video, count] of videoLogs[j]) {
//                 if (viewCount[video]) {
//                     viewCount[video] += count;
//                 } else {
//                     viewCount[video] = count;
//                 }
//             }
//         }

//         // Find the most viewed video, resolving ties alphabetically
//         let maxViews = -1;
//         let topVideo = "";

//         for (const video in viewCount) {
//             const count = viewCount[video];
//             if (count > maxViews || (count === maxViews && video < topVideo)) {
//                 maxViews = count;
//                 topVideo = video;
//             }
//         }

//         result.push(topVideo);
//     }

//     return result;
// }

// // Example usage:
// const videoLogs: [string, number][][] = [
//     [['video1', 1], ['video2', 1], ['video3', 1]],
//     [['video1', 2], ['video2', 3]],
//     [['video2', 1], ['video1', 1], ['video3', 1]],
//     [['video3', 2], ['video2', 1]],
//     [['video1', 1], ['video2', 1]]
// ];
// const windowSize = 3;

// console.log(videoCache(videoLogs, windowSize)); // Output: ['video2', 'video2', 'video1', 'video1']

function videoCache(videoLogs: [string, number][][], window: number): string[] {
    const result: string[] = [];
    const n = videoLogs.length;

    for (let i = 0; i <= n - window; i++) {
        const viewCount: { [key: string]: number } = {};

        // Sum up the views for the current window
        for (let j = i; j < i + window; j++) {
            for (const [video, count] of videoLogs[j]) {
                if (viewCount[video]) {
                    viewCount[video] += count;
                } else {
                    viewCount[video] = count;
                }
            }
        }

        // Find the most viewed video, resolving ties alphabetically
        let maxViews = -1;
        let topVideo = "";

        for (const video in viewCount) {
            const count = viewCount[video];
            if (count > maxViews || (count === maxViews && video < topVideo)) {
                maxViews = count;
                topVideo = video;
            }
        }

        result.push(topVideo);
    }

    return result;
}

// Example usage:
const videoLogs: [string, number][][] = [
    [['video1', 1], ['video2', 1]],
    [['video2', 1], ['video3', 1]],
    [['video1', 1], ['video2', 1]],
    [['video1', 1], ['video2', 1]],
    [['video1', 1], ['video2', 1]],
    [['video1', 1], ['video2', 1]]
];

console.log(videoCache(videoLogs, 3)); // Output: ['video2', 'video2', 'video1', 'video1']
