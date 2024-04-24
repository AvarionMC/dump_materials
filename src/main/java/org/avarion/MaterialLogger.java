package org.avarion;

import org.bukkit.Material;
import org.bukkit.block.data.BlockData;
import org.bukkit.plugin.java.JavaPlugin;

import java.io.File;
import java.util.Arrays;
import java.util.Comparator;

public class MaterialLogger extends JavaPlugin {

    @Override
    public void onEnable() {
        saveDefaultConfig();
        getServer().getScheduler().runTask(this, () -> {
            Material[] materials = Material.values();
            Arrays.sort(materials, Comparator.comparing(Enum::name));

            for (Material material : materials) {
                getLogger().info("Material: " + material.getKey());
                try {
                    BlockData data = material.createBlockData();
                    getLogger().info("false|" + data.getAsString(false));
                    getLogger().info("true|" + data.getAsString(true));
                } catch (Exception ex) {
                    getLogger().severe(" --> cannot create block data!");
                }
            }
            getServer().shutdown();
        });
    }
}
