import java.io.File;
import java.io.IOException;
import jakarta.servlet.http.Part;

public class FileUploadUtil {

    public static String saveFile(Part filePart, String uploadDir) throws IOException {
        // Get original filename
        String fileName = filePart.getSubmittedFileName();

        // Create uploads directory if it doesn't exist
        File directory = new File(uploadDir);
        if (!directory.exists()) {
            directory.mkdirs();
        }

        // Full path to save the file
        String filePath = uploadDir + File.separator + fileName;

        // Save the file
        filePart.write(filePath);

        return filePath;
    }
}