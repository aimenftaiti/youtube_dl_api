import ytdl from "ytdl-core";

export const download = async (req,res)=> {
    const videoUrl = req.query.videoUrl;
    try {
        const info = await ytdl.getInfo(videoUrl);
        console.log(info.videoDetails.title);
        res.setHeader("Content-Disposition", 'attachment;filename='+ info.videoDetails.title +".mp4");
        console.log(res);
        ytdl(videoUrl).pipe(res);
    } catch (err) {
        console.log(err);
        throw err;
    }
}