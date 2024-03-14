## Introduction

This repository contains a Python script that allows you to fetch video transcripts from a YouTube channel.

## Installation

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/imomayiz/youtube_scraper.git
   ```

2. Navigate to the `youtube_scraper` directory:

3. Install the necessary dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `youtube_scraper` directory and add your YouTube API key. The `.env` file should contain the following line:

   ```
   YOUTUBE_API_KEY=your-api-key
   ```

   Replace `your-api-key` with your actual YouTube API key. For more details on how to create a youtube api key, follow this [guide](https://medium.com/@momayiz.imane/scraping-youtube-video-transcripts-5e3edee5656b).


## Usage

To fetch video transcripts from a YouTube channel, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the `youtube_scraper` directory:

   ```
   cd youtube_scraper
   ```

3. Run the following command to execute the script:

   ```
   python ytb_scraper.py --channel_name "your-channel-name" --results_dir "path-to-save-transcripts" --max_videos 10
   ```

   Replace `your-channel-name` with the name of the YouTube channel you want to fetch transcripts from. Replace `path-to-save-transcripts` with the directory where you want to save the transcripts. The `--max_videos` argument is optional and allows you to limit the number of videos to fetch a transcript for.

4. The script will start fetching the transcripts from all videos in the specified channel and save them in separate text files.

**N.B.** Not all videos have a transcript!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.