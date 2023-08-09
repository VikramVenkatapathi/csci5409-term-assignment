import AWS from 'aws-sdk';
import sharp from 'sharp';

const s3 = new AWS.S3();

export const handler = async (event) => {
  try {
    const bucketName = event.bucket_name;
    const objectKey = event.object_key;
    const detectedLabels = event.detected_labels;
    const userEmail = objectKey.split('/')[0];

    // Get the original image from S3
    const s3Response = await s3.getObject({ Bucket: bucketName, Key: objectKey }).promise();
    const imageContent = s3Response.Body;

    // Apply annotations to the image
    const annotatedImage = await applyAnnotations(imageContent, detectedLabels, event.annotations);

    // Upload the annotated image to S3
    const objectKeyParts = objectKey.split('/');
    const fileName = objectKeyParts[objectKeyParts.length - 1];
    const annotatedImageKey = `${userEmail}/annotated/${fileName}`;
    // const annotatedImageKey = `${userEmail}/annotated/${objectKey}`;
    await s3.putObject({ Bucket: bucketName, Key: annotatedImageKey, Body: annotatedImage }).promise();

    return {
      statusCode: 200,
      body: 'Image annotation completed!',
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Error occurred during image annotation', error: error.message }),
    };
  }
};

async function applyAnnotations(imageContent, detectedLabels, annotations) {
  // Create a Sharp image object from the image content
  const image = sharp(imageContent);

  // Placeholder code: Draw bounding boxes and labels
  const metadata = await image.metadata();
  const width = metadata.width;
  const height = metadata.height;

  // Draw red bounding boxes and labels
  const annotatedImage = await image
    .clone()
    .composite([
      {
        input: Buffer.from(
          `<svg>
            ${detectedLabels.map((label) => {
              const annotation = annotations.find((ann) => ann.label === label);
              if (annotation) {
                const { width, height, left, top } = annotation.bounding_box;
                return `<rect x="${left * width}" y="${top * height}" width="${width}" height="${height}" stroke="red" fill="transparent" stroke-width="3"/>
                        <text x="${left * width}" y="${top * height}" fill="red" font-size="16">${label}</text>`;
              } else {
                return '';
              }
            })}
          </svg>`
        ),
      },
    ])
    .toBuffer();

  return annotatedImage;
}
